import re
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright  # Correctly import sync_playwright

def clean_url(url):
    """
    Cleans the URL by removing any extraneous characters like commas, quotes, etc.
    """
    return url.strip().strip('"').strip(',')  # Removes leading/trailing spaces, quotes, and commas

def check_status_with_playwright(url, expected_status_code):
    """
    Use Playwright to check the URL and get its status code and page content.
    """
    try:
        with sync_playwright() as p:
            # Launch a browser instance (Chromium by default)
            browser = p.chromium.launch(headless=True)  # Run in headless mode (no GUI)
            page = browser.new_page()

            # Navigate to the URL
            page.goto(url)

            # Get the status code of the page (status code can be fetched directly from browser context)
            status_code = page.evaluate('() => document.readyState')  # 'complete' when the page is loaded

            # Get the page source (HTML content)
            body = page.content()

            # Check if the body contains the specified status code text (e.g., 404, 500, etc.)
            status_code_text = str(expected_status_code)
            if status_code_text in body:
                print(f"Status code {status_code_text} found in the body for {url}")
                return None  # Skip the URL if the status code is found in the body

            # If status code doesn't match, return URL and body content
            return url, status_code, body

    except Exception as e:
        print(f"Error with {url}: {e}")
        return None

def extract_urls(input_data):
    """Extracts all URLs from the input data using regex."""
    url_pattern = r'(https?://[^\s]+|ftp://[^\s]+)'  # Regex to match URLs
    return re.findall(url_pattern, input_data)

def main():
    parser = argparse.ArgumentParser(description="Extract URLs and check for a specified status code and content.")
    parser.add_argument('-sc', '--status_code', type=int, required=True, help="The status code to filter for (e.g., 404, 500)")
    parser.add_argument('-o', '--output', type=str, required=True, help="Output file to write valid URLs")
    parser.add_argument('-t', '--threads', type=int, default=10, help="Number of threads to use for concurrent processing")

    args = parser.parse_args()

    # Read input from file or stdin
    if not sys.stdin.isatty():  # if input is piped in
        input_data = sys.stdin.read()
    else:  # if input is from a file
        input_file = input("Enter the target file name: ").strip()
        with open(input_file, 'r') as f:
            input_data = f.read()

    # Extract URLs from input data
    urls = extract_urls(input_data)

    # Process each URL and filter based on status code using multithreading
    valid_urls = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        # Submit tasks to the thread pool
        future_to_url = {executor.submit(check_status_with_playwright, clean_url(url), args.status_code): url for url in urls}

        for future in future_to_url:
            result = future.result()  # Wait for the task to complete
            if result:
                url, status_code, body = result
                # If the status code doesn't match, add it to the valid URLs
                if status_code != args.status_code:
                    valid_urls.append(f"URL: {url}\nStatus Code: {status_code}\nBody:\n{body}\n")

    # Write valid URLs with status code and body to the output file
    if valid_urls:
        with open(args.output, 'w') as output_file:
            for valid_url in valid_urls:
                output_file.write(valid_url + '\n\n')  # Add newlines between results for readability
        print(f"Valid URLs and their details saved to {args.output}")
    else:
        print("No valid URLs found.")

if __name__ == "__main__":
    main()
