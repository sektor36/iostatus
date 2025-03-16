
# IOStatus Message URL Checker - 🚀 The Ultimate Tool for Filtering Valid URLs

## 💡 What Is the Status Message URL Checker?

The **Status Message URL Checker** is a powerful Python tool designed for web security researchers, bug bounty hunters, and penetration testers to efficiently filter out URLs that display certain status messages (e.g., "404 Not Found", "500 Internal Server Error") in their page content. This tool helps verify that URLs do not contain false positives related to error status pages, which is essential for tasks like web scraping, directory scanning, and security assessments.

### Why You Should Use It

1. **Eliminate False Positives:**
   During web security testing or directory brute-forcing, you might encounter pages that return a **200 OK** status but display error messages like "404 Not Found". These are false positives, suggesting the directory or resource exists but the content indicates otherwise. This tool filters those URLs out, saving time and resources.

2. **Automate the Detection of Specific Status Messages:**
   Websites may return **200 OK** responses but display errors like **"500 Internal Server Error"** in the body of the page. This tool automates the detection of such discrepancies, ensuring you're only working with valid pages.

3. **Customizable and Flexible:**
   - **Specify Custom Status Messages:** You can search for any text (e.g., "404", "Page Not Found", "500 Error") within the page content.
   - **Multi-threading:** Efficiently handle large URL lists with concurrent processing, speeding up your scanning process.
   - **Delay Option:** Introduce a delay between requests to avoid overwhelming the target server, ensuring ethical scraping practices.

---

## 🛠️ Features

- **Search & Filter by Status Message:** Exclude URLs that contain specific error messages like "404 Not Found" or "500 Internal Server Error".
- **Multi-threading Support:** Handle large lists of URLs by processing them concurrently, significantly improving performance.
- **Customizable Status Message:** Search for any status message in the page content (not just HTTP status codes).
- **Outputs Valid URLs:** Only URLs that do not contain the error message will be saved and printed.
- **Adjustable Delay Between Requests:** Add delays between requests to prevent overloading the server.
- **Terminal Feedback:** Get real-time updates in the terminal, showing which URLs are valid.

---

## 🌐 Best Case Scenarios for Use

### 1. **Web Security Assessments**
   When performing a security assessment or vulnerability scanning, it's crucial to verify the existence of certain resources across a website. This tool ensures you only work with URLs that lead to valid content, avoiding false positives.

   **Example Use Case:**
   Penetration testers use this tool to scan a target website for directories while excluding error pages that contain status messages like "404 Not Found" or "500 Internal Server Error".

### 2. **Web Scraping & Directory Brute-Forcing**
   If you're running a directory brute-forcing tool like **Feroxbuster** or **Dirbuster**, you might encounter numerous false positives due to custom error pages. This tool filters out invalid results, focusing on valid pages.

   **Example Use Case:**
   Bug bounty hunters can integrate this tool into their brute-forcing scripts to filter out errors and avoid wasting time on non-existent resources.

### 3. **Validating Large Lists of URLs**
   Whether you have URLs scraped from a website or generated from a brute-force tool, this script helps filter them to ensure you’re only working with live, valid URLs.

   **Example Use Case:**
   SEO professionals can use this tool to validate URLs to ensure their rankings and indexing are not affected by invalid pages.

---

## 📦 Requirements

- Python 3.6 or higher
- **Playwright** for browser automation (install necessary browser binaries)

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sektor36/iostatus.git
   cd iostatus
   ```

2. Install Playwright:

   ```bash
   pip install playwright
   python -m playwright install
   ```

---

## 📋 Usage

The tool reads a list of URLs, searches for a specific status message in the page content, and excludes URLs containing that message. The valid URLs will be printed in the terminal and saved to the output file.

### 🧑‍💻 Example Workflow:

If you have a file (`target-urls.txt`) containing a list of URLs you want to check, and you want to filter out "404 Not Found" error pages, you can run:

```bash
cat target-urls.txt | python iostatus.py -sm "404 Not Found" -o valid_urls.txt -t 20 -d 1
```

### 📝 Example Output:

#### Terminal Output:
```
Valid URL found: https://example.com/valid-page-1
Valid URL found: https://example.com/valid-page-2
```

#### Output File (`valid_urls.txt`):
```
https://example.com/valid-page-1
https://example.com/valid-page-2
https://example.com/another-valid-page
```

---

## 💡 Advanced Usage

- **Increase Threads for Faster Execution:** If you have a large number of URLs, increase the number of threads to speed up processing:

  ```bash
  python iostatus.py -sm "404 Not Found" -o results.txt -t 50 -d 0.1
  ```

- **Custom Status Message:** You can change the status message you're looking for (e.g., "Page Not Found"):

  ```bash
  python iostatus.py -sm "Page Not Found" -o filtered_urls.txt -t 10 -d 0.5
  ```

---

## 🔍 How It Works

1. **Clean URL Input:** The URLs are first cleaned by stripping extra spaces, quotes, or commas.
2. **Playwright Automation:** The tool uses **Playwright** to visit each URL in **headless mode** (without opening a browser window) and retrieve the page content.
3. **Search for Status Message:** It checks the body content of each page for the specified status message (e.g., "404 Not Found").
4. **Filter Invalid URLs:** If the status message is found, the URL is excluded. Only valid URLs (those without the error message) are processed.
5. **Output Results:** Valid URLs are printed in the terminal and saved to the specified output file. Optionally, you can add delays between requests to reduce server load.

---

## 📝 Notes

- The script operates in **headless mode** (without opening a browser window) to ensure fast execution.
- Be considerate when running this tool on a live site. If scanning a large number of URLs, use the `-d` delay argument to avoid overwhelming the target server.
- **Playwright** ensures dynamic content is rendered properly, which means the tool works even on pages that rely on JavaScript to load content.

---

## 📄 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

