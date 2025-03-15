import re
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright

def clean_url(url):
    return url.strip().strip('"').strip(',')

def check_status_with_playwright(url, status_message):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url)

            body = page.content()  # Get the body content of the page

            if status_message.lower() in body.lower():  # Check if the status message is found in the body
                print(f"Found '{status_message}' in the body for {url}")
                return url, body

            return None

    except Exception as e:
        print(f"Error with {url}: {e}")
        return None

def extract_urls(input_data):
    url_pattern = r'(https?://[^\s]+|ftp://[^\s]+)'
    return re.findall(url_pattern, input_data)

def main():
    parser = argparse.ArgumentParser(description="Extract URLs and check for a specified status message in the body.")
    parser.add_argument('-sm', '--status_message', type=str, required=True, help="The status message to search for in the page body (e.g., '404 not found')")
    parser.add_argument('-o', '--output', type=str, required=True, help="Output file to write URLs containing the status message")
    parser.add_argument('-t', '--threads', type=int, default=10, help="Number of threads to use for concurrent processing")

    args = parser.parse_args()

    if not sys.stdin.isatty():  # If input is piped in
        input_data = sys.stdin.read()
    else:  # If input is from a file
        input_file = input("Enter the target file name: ").strip()
        with open(input_file, 'r') as f:
            input_data = f.read()

    urls = extract_urls(input_data)

    valid_urls = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_url = {executor.submit(check_status_with_playwright, clean_url(url), args.status_message): url for url in urls}

        for future in future_to_url:
            result = future.result()
            if result:
                url, body = result
                valid_urls.append(f"URL: {url}\nBody:\n{body}\n")

    if valid_urls:
        with open(args.output, 'w') as output_file:
            for valid_url in valid_urls:
                output_file.write(valid_url + '\n\n')
        print(f"Valid URLs with the status message saved to {args.output}")
    else:
        print("No valid URLs found.")

if __name__ == "__main__":
    main()
