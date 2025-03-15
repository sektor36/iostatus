`iostatus.py` is a tool designed to help web security researchers and bug bounty hunters identify pages with specific status messages in the body of the page content. It is especially useful for filtering out **false positives** when using tools like Feroxbuster, where pages may return a `200 OK` status with a custom error message (e.g., `"404 Not Found"`) in the body, misleading you into thinking the directory exists.

### Why was this tool created?

This tool was created because many web applications have custom 404 error pages. These error pages can return a `200 OK` HTTP status code, but the body of the page contains a message such as `"404 Not Found"` or `"Page not found"`. In cases like this, it's important to find a way to accurately detect those pages based on the message within the body content, rather than relying solely on the status code.

## Features

- **Search for status messages in page content**: Specify a string to search for within the body of the page (e.g., "404 Not Found").
- **Concurrency with threads**: Supports multi-threaded processing to quickly check a list of URLs.
- **Flexible output**: Write the URLs that match the specified status message to an output file.
- **Works with URLs from files or pipes**: Can take input URLs from a file or stdin.

---

## Installation

Before using this script, ensure that you have the following dependencies installed:

1. **Python 3.7+**
2. **Playwright** (Install via `pip`):

```bash
pip install playwright
python -m playwright install
```

---

## Usage

### Command Syntax

```bash
python iostatus.py -sm "status message" -o output_file -t threads
```

- `-sm` (Required): The status message to search for in the body of the page (e.g., `"404 Not Found"`, `"Page not found"`, etc.).
- `-o` (Required): The output file where URLs with matching status messages will be saved.
- `-t` (Optional): The number of threads to use for concurrent processing (default is 10).

---

### Example Usage

To search for URLs that contain the message `"404 Not Found"` in the body and save them to `results.txt`, run the following command:

```bash
cat target-urls.txt | python iostatus.py -sm "404 Not Found" -o results.txt -t 10
```

- **`target-urls.txt`**: A text file containing a list of URLs to check.
- **`-sm "404 Not Found"`**: Look for the message `"404 Not Found"` in the body of the page.
- **`-o results.txt`**: Save the matching URLs to `results.txt`.
- **`-t 10`**: Use 10 concurrent threads to speed up the process.

### Example Output in `results.txt`

```
URL: https://example.com/some-page
Body:
Page not found. The page you are looking for might have been removed or is temporarily unavailable.

URL: https://example.com/another-page
Body:
404 Not Found
The page you requested could not be found.
```

---

## How It Works

1. **Extract URLs**: The script takes input URLs from a file or stdin.
2. **Search for Status Message**: It loads each page using Playwright and searches for the status message you specify in the body content.
3. **Filter and Output**: If the status message is found in the page's body, the URL and the body content are saved to the output file.

---

## Why Use This Tool?

Many web directories and pages may return `200 OK` HTTP status codes, even though the content on the page indicates an error (such as a `404 Not Found` page). This tool allows you to filter out such pages by specifying a status message string to search for, ensuring that only relevant URLs are returned.

---

## License

This tool is released under the MIT License. See `LICENSE` for more details.

