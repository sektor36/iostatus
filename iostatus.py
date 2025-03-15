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
            body = page.content()
            if status_message in body:
                return None  # Skip URLs with the specified status message
            return url  # Return the URL if it doesn't match the status message
    except Exception as e:
        print(f"Error with {url}: {e}")
        return None

def extract_urls(input_data):
    url_pattern = r'(https?://[^\s]+|ftp://[^\s]+)'
    return re.findall(url_pattern, input_data)

def main():
    parser = argparse.ArgumentParser(description="Extract URLs and filter out those with the specified status message in the body.")
    parser.add_argument('-sm', '--status_message', type=str, required=True, help="The status message to search for in the body (e.g., '404 Not Found')")
    parser.add_argument('-o', '--output', type=str, required=True, help="Output file to write valid URLs")
    parser.add_argument('-t', '--threads', type=int, default=10, help="Number of threads to use for concurrent processing")

    args = parser.parse_args()

    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
    else:
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
                valid_urls.append(result)

    if valid_urls:
        with open(args.output, 'w') as output_file:
            for valid_url in valid_urls:
                output_file.write(valid_url + '\n')
        print(f"Valid URLs saved to {args.output}")
    else:
        print("No valid URLs found.")

if __name__ == "__main__":
    main()
