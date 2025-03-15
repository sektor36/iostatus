
# Status Message URL Checker

This Python tool helps web security researchers, bug bounty hunters, and penetration testers filter out URLs that contain specific status messages (like "404 Not Found", "500 Internal Server Error", etc.) in the body of the page. It is especially useful when dealing with custom 404 pages or pages where the status code doesn’t accurately reflect the content (e.g., a page returning a 200 status but containing a "404 Not Found" message in the body).

### 🚀 Why Was This Tool Created?

Often, web directory brute-force tools like **Feroxbuster** or **Dirbuster** can generate false positives when a target website uses custom error pages (e.g., a "404 Not Found" page that returns a `200 OK` status). These tools may report that a directory exists, even though it doesn't. This tool was designed to help eliminate those false positives by searching the content of the page for a specific **status message** that you specify (like "404" or "404 Not Found") and exclude those URLs from the final results.

### 🔧 Features

- **Search and Filter by Status Message**: Search for a specific string (e.g., "404 Not Found") in the body of the page and filter out URLs that contain it.
- **Multi-threading Support**: Process URLs concurrently using multiple threads for faster results.
- **Customizable Search String**: Specify any status message (e.g., "404", "Page Not Found", "500 Server Error") to match against the page's body content.
- **Output Non-Matching URLs**: Save only the URLs that do not contain the specified status message to an output file.

### 📦 Requirements

- Python 3.6+
- Install the necessary dependencies with:

  ```bash
  pip install playwright
  ```

  *Note: You'll need `playwright` for browser automation.*

### 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sektor36/iostatus.git
   cd iostatus
   ```

2. **Install Playwright Browsers**:

   After installing Playwright, you'll need to install the necessary browser binaries:

   ```bash
   python -m playwright install
   ```

---

### 📋 Usage

1. **Basic usage**:

   To run the tool, provide the following arguments:

   - `-sm`/`--status_message`: The status message (e.g., "404 Not Found") to search for in the page body.
   - `-o`/`--output`: The output file to write URLs that **do not** contain the status message.
   - `-t`/`--threads`: Number of threads to use for concurrent processing (default: 10).

   Example:

   ```bash
   cat target-urls.txt | python iostatus.py -sm "404 Not Found" -o valid_urls.txt -t 10
   ```

   - This will **search** for the string `"404 Not Found"` in the body of each page and exclude those URLs from the output.
   - The valid URLs that **do not contain** the specified status message will be saved to `valid_urls.txt`.

---

### 🧑‍💻 Example Workflow

Assume you're scanning a target website for directories, and you have a file (`target-urls.txt`) containing a list of URLs. Some of these URLs might return a `200 OK` status but display a "404 Not Found" message in the page content.

You can run the tool as follows:

```bash
cat target-urls.txt | python iostatus.py -sm "404 Not Found" -o results.txt -t 20
```

This command will:

- Read the URLs from `target-urls.txt`.
- Check each URL's page content for the string `"404 Not Found"`.
- **Print** the message to the terminal when it finds that string, e.g., `404 Not Found found in this page: https://example.com/404-page`.
- **Write** only the URLs that do **not** contain `"404 Not Found"` to `results.txt`.

### 📝 Example Output

#### Terminal Output

When a status message is found in the body of a page:

```
404 Not Found found in this page: https://example.com/404-page
500 Internal Server Error found in this page: https://example.com/500-error-page
```

#### Output File (`results.txt`)

The URLs that **do not** contain the specified status message will be written to the output file, like so:

```
https://example.com/valid-page-1
https://example.com/valid-page-2
https://example.com/another-valid-page
```

---

### 💡 Advanced Usage

You can run the tool with more specific arguments based on your needs:

1. **Specify a custom status message**:
   
   ```bash
   python iostatus.py -sm "Page Not Found" -o filtered_urls.txt -t 5
   ```

2. **Process URLs with more threads for faster execution**:

   ```bash
   python iostatus.py -sm "404 Not Found" -o clean_urls.txt -t 50
   ```

---

### 🔍 How It Works

1. **Clean URL Input**: URLs from a provided file or stdin are cleaned up (i.e., removed extra spaces, commas, quotes).
2. **Playwright Automation**: The script uses Playwright to visit each URL and retrieve the body content.
3. **Search for Status Message**: It checks if the page's body contains the specified status message (e.g., "404 Not Found").
4. **Filter URLs**: URLs containing the status message in the body are excluded from the output.
5. **Write Results**: URLs that **do not** contain the specified message are saved to an output file.

---

### 📝 Notes

- This tool uses **Playwright**, a browser automation library, for dynamic content rendering. Make sure the necessary browsers are installed using the `python -m playwright install` command.
- The script runs in headless mode (without opening the browser window) for performance.
- If you are scanning a large number of URLs, be mindful of the number of threads you use to avoid overwhelming the target server.

---

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

