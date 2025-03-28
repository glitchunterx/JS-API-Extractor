import os
import re
import requests

# File containing JS URLs
JS_LINKS_FILE = "js_links.txt"

# Directory to save downloaded JS files
JS_DIR = "./downloaded_js"

# Output file for matched results
OUTPUT_FILE = "extracted_results.txt"

# Create directory if not exists
os.makedirs(JS_DIR, exist_ok=True)

# Keywords to search for
KEYWORDS = ["POST", "GET", "api", "graphql", "fetch", "axios", ".json"]

# Regex pattern to match lines containing any keyword
KEYWORD_PATTERN = re.compile(r'("|\')?(POST|GET|api|graphql|fetch|axios|\.json)("|\')?', re.IGNORECASE)

def download_js_files():
    """Download JS files from URLs in js_links.txt."""
    with open(JS_LINKS_FILE, "r") as f:
        links = f.readlines()

    for link in links:
        link = link.strip()
        if not link:
            continue
        
        try:
            response = requests.get(link, timeout=10)
            if response.status_code == 200:
                file_name = os.path.join(JS_DIR, os.path.basename(link))

                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(response.text)
                
                print(f"Downloaded: {file_name}")
            else:
                print(f"Failed: {link} (Status: {response.status_code})")
        except requests.RequestException as e:
            print(f"Error downloading {link}: {e}")

def extract_relevant_lines():
    """Extract lines containing specified keywords from JS files."""
    results = []

    for file_name in os.listdir(JS_DIR):
        if file_name.endswith(".js"):
            file_path = os.path.join(JS_DIR, file_name)

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if KEYWORD_PATTERN.search(line):
                            results.append(f"File: {file_path} → {line.strip()}")

            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(results))

    print(f"Extracted results saved in {OUTPUT_FILE}")

# Execute functions
download_js_files()
extract_relevant_lines()

