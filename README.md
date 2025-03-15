

# Status Message URL Checker - 🚀 The Ultimate Tool for Filtering Valid URLs

## 💡 What Is the **Status Message URL Checker**?

The **Status Message URL Checker** is a powerful Python tool that helps web security researchers, bug bounty hunters, and penetration testers to efficiently filter out URLs that display certain status messages (e.g., "404 Not Found", "500 Internal Server Error") in their page content. Often used in web scraping, directory scanning, and security assessments, this tool ensures you're working with **valid** URLs that **do not** have false positives related to status message pages.

This tool is especially useful when a website returns **incorrect status codes**, such as when it returns `200 OK` but displays a "404 Not Found" message or other server errors in the body of the page. It provides a reliable way to verify the real content of a webpage.

---

## 🚀 Why You Should Use It

### **1. Eliminate False Positives:**
During web security testing or directory brute-forcing, you might encounter pages that return a `200 OK` status but display error messages like "404 Not Found". These are **false positives** because they suggest the directory or resource exists, but the content indicates otherwise. **Status Message URL Checker** ensures you don’t waste time or resources working with those links by filtering them out based on the status message you specify.

### **2. Automate the Detection of Specific Status Messages:**
Many websites return custom error pages or dynamically render content that causes discrepancies between the HTTP status code and the actual page content. For example, you might encounter a `200 OK` response with "500 Internal Server Error" written in the page body. This tool helps you automate the detection of such discrepancies and get only **the valid, non-error pages**.

### **3. Customizable and Flexible:**
- **Specify Custom Status Messages**: You can search for any text (e.g., "404", "Page Not Found", "500 Error") to filter pages based on their content, not just the status code.
- **Multi-threading**: Handle large URL lists efficiently with concurrent processing to speed up scanning.
- **Delay Option**: You can set delays between requests to avoid overwhelming the target server and maintain ethical scraping practices.

---

## 🛠️ Features

- **Search & Filter by Status Message**: Search for any specific status message in the page’s body content (e.g., "404 Not Found", "Page Not Found", "500 Internal Server Error") and exclude the URLs that contain those messages.
  
- **Multi-threading Support**: Use multiple threads to process URLs concurrently, significantly improving performance when dealing with large URL lists.

- **Customizable Status Message**: Specify any status message to look for within the page content.

- **Outputs Valid URLs**: Only URLs that **do not** contain the status message will be written to the output file and printed in the terminal.

- **Adjustable Delay Between Requests**: Introduce delays between requests to avoid putting excessive load on the server. This feature is especially important for ethical web scraping.

- **Terminal Feedback**: See which URLs are valid in real time with detailed messages printed directly in the terminal, such as `Valid URL found: https://example.com/valid-page`.

---

## 🌐 Best Case Scenarios for Use

### **1. Web Security Assessments:**
When performing a security assessment or vulnerability scanning, you might need to verify the existence of certain resources across a website. Often, a website will return a "200 OK" status code for a URL that leads to an error page. **This tool will filter those URLs out, ensuring you’re only working with URLs that lead to valid content.**

**Example Use Case:**
- **Penetration testers** can use this tool to scan a target website for directories while excluding error pages that contain status messages like "404 Not Found" or "500 Internal Server Error".

### **2. Web Scraping & Directory Brute-Forcing:**
If you're running a directory brute-forcing tool like **Feroxbuster** or **Dirbuster**, you may encounter numerous false positives due to custom error pages. This tool helps you **automatically filter out** invalid results, focusing only on **valid pages** that don’t display error messages in their content.

**Example Use Case:**
- **Bug bounty hunters** can integrate this tool with their directory brute-forcing scripts to eliminate errors and avoid wasting time on non-existent resources.

### **3. Validating Large Lists of URLs:**
Whether you have URLs scraped from a website or generated from a brute-force tool, this script helps you filter them to ensure that you’re working with live, valid URLs that don’t contain error messages.

**Example Use Case:**
- **SEO professionals** can use this tool to verify that a list of URLs does not contain errors that would affect their rankings or indexing.

---

## 📦 Requirements

- Python 3.6 or higher
- Playwright for browser automation (install the necessary browser binaries)

## 🛠️ Installation

1. Install **Playwright**:
   
   Install the Playwright library and its necessary browser binaries:

   ```bash
   pip install playwright
   python -m playwright install
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/sektor36/iostatus.git
   cd iostatus
   ```

---

## 📋 Usage

The tool works by reading a list of URLs, searching for a specific status message in the page content, and excluding URLs that contain that message. The valid URLs (those that do not contain the message) will be printed in the terminal and saved to the output file.

### 🧑‍💻 Example Workflow:

Let’s say you have a file (`target-urls.txt`) with a list of URLs you want to check. Some of these URLs might return a "404 Not Found" error page, but they may still return a `200 OK` HTTP status code. You can run the following command to filter out those invalid URLs:

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

- **Specify a Custom Status Message**: To search for a different error message, such as "Page Not Found", simply modify the `-sm` argument:

  ```bash
  python iostatus.py -sm "Page Not Found" -o filtered_urls.txt -t 10 -d 0.5
  ```

- **Increase Threads for Faster Execution**: If you have a large number of URLs, increase the number of threads to speed up processing:

  ```bash
  python iostatus.py -sm "404 Not Found" -o results.txt -t 50 -d 0.1
  ```

---

## 🔍 How It Works

1. **Clean URL Input**: The URLs are first cleaned by stripping out extra spaces, quotes, or commas.
2. **Playwright Automation**: The tool uses Playwright to visit each URL in headless mode (without opening a browser window) and retrieve the page content.
3. **Search for Status Message**: It checks the body content of each page for the specified status message (e.g., "404 Not Found").
4. **Filter Invalid URLs**: If the status message is found, the URL is excluded. Only valid URLs (those that do not contain the status message) are processed further.
5. **Output Results**: Valid URLs are printed in the terminal and saved to the specified output file. Optionally, delays between requests can be added to respect server load.

---

## 📝 Notes

- The script operates in **headless mode** (without opening a browser window) to ensure fast execution.
- Be considerate when running this tool on a live site. If scanning a large number of URLs, use the `-d` delay argument to avoid overwhelming the target server.
- **Playwright** ensures dynamic content is rendered properly, which means the tool works even on pages that rely on JavaScript to load content.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### Installation Instructions:

- Python 3.6+
- Install the necessary dependencies with:

  ```bash
  pip install playwright
  ```

- Clone the repository:

  ```bash
  git clone https://github.com/sektor36/iostatus.git
  cd iostatus
  ```
