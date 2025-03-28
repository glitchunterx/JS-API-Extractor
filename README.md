# JS API Extractor 🚀
A Python-based tool to **download JavaScript files from a list of URLs** and **extract API-related calls** like `fetch`, `axios`, `POST`, `GET`, `graphql`, etc.

## 🛠 Features
✅ Downloads `.js` files from URLs in `js_links.txt`  
✅ Extracts lines containing API requests (`fetch()`, `axios()`, etc.)  
✅ Saves results in `extracted_results.txt`  
✅ Fully customizable for different keywords  

## 🚀 Usage

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/JS-API-Extractor.git
cd JS-API-Extractor

2️⃣ Install Dependencies
Ensure Python is installed, then install requests (if not installed):
pip install requests

3️⃣ Add JavaScript File URLs
Edit js_links.txt and add one URL per line:
https://example.com/script1.js
https://example.com/script2.js

4️⃣ Run the Scripts
📥 Download JS Files
python3 download_and_search.py
This will store all .js files inside the downloaded_js/ folder.

🔍 Extract API Calls
python3 extract_relevant_lines.py
This will scan all downloaded JS files and save extracted lines in extracted_results.txt.


---

### **4️⃣ File Descriptions Section**

This part explains each file in the repository.
```md
## 📂 File Descriptions
| File Name                   | Description |
|-----------------------------|-------------|
| `download_and_search.py`    | Downloads JS files from URLs in `js_links.txt`. |
| `extract_relevant_lines.py` | Extracts API-related lines from JS files. |
| `js_links.txt`              | List of JS file URLs to be scanned. |
| `extracted_results.txt`     | Output file with extracted API calls. |

## 🛠 Customization  
You can modify `extract_relevant_lines.py` to **change keywords** or **improve regex patterns** according to your needs.  

Example: If you want to **add more keywords**, update:
```python
KEYWORDS = ["POST", "GET", "api", "graphql", "fetch", "axios", ".json", "new_keyword"]


---

### **6️⃣ Contributing Section**

Guidelines for others who want to contribute to the project.
```md
## 🤝 Contributing
We welcome contributions! 🎉  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-xyz`)  
3. Commit your changes (`git commit -m "Added feature XYZ"`)  
4. Push to your branch (`git push origin feature-xyz`)  
5. Open a Pull Request  

## 📜 License
This project is licensed under the **MIT License**.  
Feel free to use and modify it! 🎯  

## 👨‍💻 Author
Maintained by [glitchunter](https://github.com/glitchunterx).  
For any queries, feel free to create an **issue** or **pull request**. 🚀

