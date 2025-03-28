import os
import re
import requests

# File containing the .js links
JS_LINKS_FILE = "js_links.txt"

# Directory to save downloaded .js files
JS_DIR = "./downloaded_js"

# Keywords to search for
KEYWORDS = ["api/", "graphql", "fetch(", "axios(", "POST", "GET", ".json"]

# Output file to save search results
OUTPUT_FILE = "search_results.txt"

# Create directory if not exists
os.makedirs(JS_DIR, exist_ok=True)


def download_js_files():
    """Download JS files from the given URLs in js_links.txt."""
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
                
                # Save JS file
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(response.text)
                
                print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download: {link} (Status: {response.status_code})")
        except requests.RequestException as e:
            print(f"Error downloading {link}: {e}")


def search_keywords():
    """Search for specified keywords in the downloaded JS files."""
    results = []

    for file_name in os.listdir(JS_DIR):
        if file_name.endswith(".js"):
            file_path = os.path.join(JS_DIR, file_name)

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                for keyword in KEYWORDS:
                    matches = re.findall(rf"{keyword}", content, re.IGNORECASE)
                    if matches:
                        results.append(f"Found '{keyword}' in {file_path}")

            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    # Save results
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(results))

    print(f"Results saved in {OUTPUT_FILE}")


# Execute functions
download_js_files()
search_keywords()

