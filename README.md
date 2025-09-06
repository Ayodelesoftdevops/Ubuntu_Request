🖼️ Ubuntu Image Fetcher

A command-line tool for mindfully collecting images from the web — built with Ubuntu values of community, respect, sharing, and practicality.

🌍 Overview

This Python script allows users to input multiple image URLs and downloads them to a local folder while:

Preventing duplicate downloads

Verifying that each URL is a valid image

Handling connection errors gracefully

Automatically generating filenames when needed

✅ Features

🧠 Multiple URL input (one at a time)

🔒 Safe downloading (validates Content-Type as image)

🔁 Duplicate detection using content hashing (MD5)

📁 Organized saving in a dedicated Fetched_Images folder

🛡️ Robust error handling for connection and unexpected issues

💬 Ubuntu values reflected in user-friendly messaging

💻 How to Use
1. Clone or Download

Save the script to your machine as ubuntu_image_fetcher.py.

2. Install Required Package

Make sure requests is installed:

pip install requests

3. Run the Script

In your terminal or VS Code:

python ubuntu_image_fetcher.py

4. Input URLs

You’ll be prompted to enter image URLs one at a time:

Please enter the image URL: https://example.com/image1.jpg
Please enter the image URL: https://example.com/photo.png
Please enter the image URL: done

📂 Output

Downloaded images will be saved in a folder:

Fetched_Images/
├── image1.jpg
├── photo.png


Duplicate images (based on content hash) will not be saved again.

🧪 Example Output
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/image1.jpg
✓ Successfully fetched: image1.jpg
✓ Image saved to Fetched_Images/image1.jpg

Please enter the image URL: https://example.com/duplicate.jpg
⏩ Skipped duplicate image from: https://example.com/duplicate.jpg

Please enter the image URL: https://example.com/fake.exe
✗ Skipped: Not an image - https://example.com/fake.exe

Please enter the image URL: done
Connection strengthened. Community enriched.

🛠️ How It Works

URL Parsing: Uses urlparse to extract filenames.

Content Validation: Uses the Content-Type header to ensure the file is an image.

Hashing: Generates a unique hash using hashlib.md5 to prevent duplicate downloads.

Error Handling: Catches connection issues using requests.exceptions.

📜 Ubuntu Principles in Action
Principle	Implementation Example
Community	Downloads from the web and shares locally
Respect	Validates and filters bad content types; handles errors cleanly
Sharing	Stores in a centralized, shareable folder
Practicality	Solves a real-world task of organized image collection
📌 Requirements

Python 3.6+

requests library

Install with:

pip install requests

📁 Project Structure
ubuntu_image_fetcher.py
README.md
Fetched_Images/     ← Created automatically after first run

🔧 To-Do Ideas (for Enhancement)

 Accept URLs from a .txt file

 GUI version using Tkinter or PyQt

 Progress bar for large downloads

 Logging of download history

📄 License

This project is shared for educational purposes and learning only.
