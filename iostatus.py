import re
import argparse
import sys
import time
import signal
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright
import os
import sys

def clean_url(url):
    return url.strip().strip('"').strip(',')

def check_status_with_playwright(url, expected_status_message, delay):
    """
    Use Playwright to check the URL and get its body content. Introduces a delay between requests.
    """
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url)

            body = page.content()

            # Check if expected status message is not in the body
            if expected_status_message not in body:
                print(f"Valid URL: {url}")  # Print only valid URLs that do not contain the expected status message
                return url  # Return the valid URL

            time.sleep(delay)  # Introduce a delay between requests

            return None  # Return None for invalid URLs

    except Exception:
        return None  # Suppress all exceptions

def extract_urls(input_data):
    """Extracts all URLs from the input data using regex."""
    url_pattern = r'(https?://[^\s]+|ftp://[^\s]+)'
    return re.findall(url_pattern, input_data)

def handle_shutdown_signal(signal, frame):
    """Handle shutdown on Ctrl + C."""
    print("\nReceived shutdown signal (Ctrl + C). Exiting...")
    os._exit(0)  # Forcefully exit the script without any further processing

def main():
    # Register the signal handler for SIGINT (Ctrl + C)
    signal.signal(signal.SIGINT, handle_shutdown_signal)

    parser = argparse.ArgumentParser(description="Extract URLs and check for a specified status message in the body.")
    parser.add_argument('-sm', '--status_message', type=str, required=True, help="The status message to search for in the body (e.g., '404 Not Found')")
    parser.add_argument('-o', '--output', type=str, required=True, help="Output file to write valid URLs")
    parser.add_argument('-t', '--threads', type=int, default=10, help="Number of threads to use for concurrent processing")
    parser.add_argument('-d', '--delay', type=float, default=0, help="Delay between requests in seconds (default is 0)")

    args = parser.parse_args()

    # Read input from file or stdin
    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
    else:
        input_file = input("Enter the target file name: ").strip()
        with open(input_file, 'r') as f:
            input_data = f.read()

    # Extract URLs from input data
    urls = extract_urls(input_data)

    # Process each URL and filter based on status message using multithreading
    valid_urls = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        # Submit tasks to the thread pool
        future_to_url = {executor.submit(check_status_with_playwright, clean_url(url), args.status_message, args.delay): url for url in urls}

        for future in future_to_url:
            result = future.result()  # Wait for the task to complete
            if result:
                valid_urls.append(result)

    # Write valid URLs to the output file
    if valid_urls:
        with open(args.output, 'w') as output_file:
            for valid_url in valid_urls:
                output_file.write(valid_url + '\n')  # Write each valid URL to a new line
        print(f"Valid URLs saved to {args.output}")
    else:
        print("No valid URLs found.")

if __name__ == "__main__":
    main()
