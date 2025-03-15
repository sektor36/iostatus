# iostatus
Status Code URL Checker Tool
Certainly! Here's the updated README that includes an explanation of why the tool was created, addressing the issue with false positives from **Feroxbuster** due to custom 404 pages:

---

# **Status Code URL Checker Tool**

## Overview

The **Status Code URL Checker** tool was created to address the issue of false positives encountered when using **Feroxbuster** or similar web directory discovery tools, particularly when the target website has custom 404 pages.

### The Problem

While performing directory and file discovery with tools like **Feroxbuster**, many security researchers and bug bounty hunters encounter false positives when the target website returns a `200 OK` response with a **custom 404 page** inside the body of the response. This typically happens when the server doesn't return an actual `404 Not Found` status code, but instead serves a `200 OK` response with a custom page that includes a "404 Not Found" message within its HTML content.

This discrepancy can lead to inaccurate findings, as the target website technically returns a successful HTTP response (`200 OK`), but the content clearly indicates the resource is missing.

### The Solution

The **Status Code URL Checker** tool was created to help solve this problem. By checking the **status code** as well as inspecting the **body** of the page, it filters out false positives caused by custom 404 pages. The tool works by allowing you to:
- Extract URLs from a file or piped input.
- Check each URL for a specified status code (e.g., `404`).
- Inspect the page content to ensure the body doesn't contain misleading status code information (e.g., "404" displayed in the page but the status code is `200`).
- Output valid URLs that match the desired criteria (status code different from the specified one).

## Features

- Extract URLs from files or stdin.
- Check each URL for a specified status code.
- Filter URLs based on the specified status code (e.g., `404`).
- Supports multithreading for faster execution.
- Output results with detailed status code and body content.

## Installation

Before using this tool, ensure that **Playwright** is installed. If it's not already installed, you can run the following commands:

```bash
pip install playwright
python -m playwright install
```

This will install the required dependencies and download the necessary browser binaries.

## Usage

### Syntax

```bash
python iostatus.py -sc <status_code> -o <output_file> -t <number_of_threads>
```

- **`-sc`**: The HTTP status code to filter for (e.g., `404`, `500`).
- **`-o`**: The output file to save valid URLs.
- **`-t`**: The number of threads to use for concurrent processing (default is 10).

### Example

Let’s say you have a file named `urls.txt` that contains a list of URLs. You can use the following command to check each URL for status code `404` and output the valid URLs to `results.txt`:

```bash
cat urls.txt | grep example.com | sort -u | python iostatus.py -sc 404 -o results.txt -t 20
```

In this example:
- **`cat urls.txt`**: This command outputs the list of URLs from `urls.txt`.
- **`grep example.com`**: This filters the URLs for those that contain `example.com`.
- **`sort -u`**: This removes duplicate URLs.
- **`python iostatus.py -sc 404 -o results.txt -t 20`**: This command runs the script to check the filtered URLs for status code `404`, using 20 threads, and saves the results to `results.txt`.

### Example from a File

1. Create a text file (`urls.txt`) containing URLs, e.g.:

   ```
   https://example.com/page1
   https://example.com/page2
   https://example.com/page3
   ```

2. Run the following command to check for status code `404`:

   ```bash
   python iostatus.py -sc 404 -o results.txt -t 10
   ```

This will output all URLs from `urls.txt` that return a status code other than `404` to the `results.txt` file.

## Example Output

The output in the `results.txt` file will look like this:

```
URL: https://example.com/page1
Status Code: 200
Body:
<html>...</html>

URL: https://example.com/page2
Status Code: 500
Body:
<html>...</html>

URL: https://example.com/page3
Status Code: 403
Body:
<html>...</html>
```

## Requirements

- Python 3.x
- Playwright
- Requests
- Argparse

## Why Was This Tool Created?

This tool was specifically created to address the **false positive issue** encountered when using **Feroxbuster** or similar directory discovery tools. Many websites have custom **404 pages** that return a `200 OK` status, despite the page content indicating that the resource is missing.

By using this tool, you can:
- Accurately filter out false positives based on status code and page content.
- Ensure that URLs with valid status codes (and not custom error pages) are included in your results.
- Save time and effort during security assessments, bug bounty hunting, or penetration testing.

## Contributing

If you'd like to contribute to the development of this tool, feel free to fork the repository, submit issues, or open pull requests. Contributions are welcome!

## License

This tool is licensed under the MIT License. See the LICENSE file for more information.

---

This updated README explains the problem the tool addresses (false positives from **Feroxbuster**) and highlights how the tool helps resolve this issue by inspecting both status codes and page content.

Let me know if you'd like further changes or additions!
