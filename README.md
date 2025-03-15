# iostatus.py

`iostatus.py` is a tool designed to help web security researchers and bug bounty hunters identify pages **without** specific status messages in the body of the page content. This tool is useful for filtering out false positives, especially when dealing with web applications that return a `200 OK` status with a custom error message (e.g., `"404 Not Found"`) in the body, which may mislead you into thinking the directory exists.

### Why was this tool created?

This tool was created to address the issue where many web applications have custom 404 error pages that return a `200 OK` status code but contain an error message like `"404 Not Found"`. In cases like this, it's important to filter out those pages based on the status message found in the body, ensuring that you're only looking at pages that do not contain the error message.

---

## Features

- **Search for status messages in page content**: Specify a string to search for within the body of the page (e.g., `"404 Not Found"`).
- **Concurrency with threads**: Supports multi-threaded processing to quickly check a list of URLs.
- **Flexible output**: Write URLs **without** the matching status message to an output file.
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
- `-o` (Required): The output file where URLs **without** the matching status message will be saved.
- `-t` (Optional): The number of threads to use for concurrent processing (default is 10).

---

### Example Usage

To search for URLs that **do not** contain the message `"404 Not Found"` in the body and save them to `results.txt`, run the following command:

```bash
cat target-urls.txt | python iostatus.py -sm "404 Not Found" -o results.txt -t 10
```

- **`target-urls.txt`**: A text file containing a list of URLs to check.
- **`-sm "404 Not Found"`**: Look for the message `"404 Not Found"` in the body of the page. Only pages **without** this message will be saved.
- **`-o results.txt`**: Save the URLs without the matching status message to `results.txt`.
- **`-t 10`**: Use 10 concurrent threads to speed up the process.

### Example Output in `results.txt`

```
https://example.com/valid-page
https://example.com/another-valid-page
```

---

## License

This tool is open-source and licensed under the MIT License. Feel free to use, modify, and distribute it for your security research needs!


