import os
import requests
from urllib.parse import urlparse
import hashlib

# Directory to save images
SAVE_DIR = "Fetched_Images"

def welcome():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

def get_urls():
    """Prompt user for multiple URLs"""
    print("Enter image URLs one by one. Type 'done' when you're finished.\n")
    urls = []
    while True:
        url = input("Please enter the image URL: ").strip()
        if url.lower() == 'done':
            break
        if url.startswith('http'):
            urls.append(url)
        else:
            print("✗ Invalid URL. It should start with http or https.")
    return urls

def create_save_dir():
    """Create the directory for saving images"""
    os.makedirs(SAVE_DIR, exist_ok=True)

def get_filename(url, content_type):
    """Extract or generate a filename based on URL and content type"""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or '.' not in filename:
        if 'jpeg' in content_type:
            filename = "downloaded_image.jpg"
        elif 'png' in content_type:
            filename = "downloaded_image.png"
        elif 'gif' in content_type:
            filename = "downloaded_image.gif"
        else:
            filename = "downloaded_image.img"
    return filename

def get_content_hash(content):
    """Generate MD5 hash of the content to detect duplicates"""
    return hashlib.md5(content).hexdigest()

def is_image(content_type):
    """Check if the content is an image"""
    return content_type.startswith('image/')

def fetch_image(url, downloaded_hashes):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type', '')
        if not is_image(content_type):
            print(f"✗ Skipped: Not an image - {url}")
            return

        image_hash = get_content_hash(response.content)
        if image_hash in downloaded_hashes:
            print(f"⏩ Skipped duplicate image from: {url}")
            return

        filename = get_filename(url, content_type)
        filepath = os.path.join(SAVE_DIR, filename)

        with open(filepath, 'wb') as file:
            file.write(response.content)

        downloaded_hashes.add(image_hash)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

def main():
    welcome()
    urls = get_urls()
    
    if not urls:
        print("✗ No valid URLs entered. Exiting.")
        return

    create_save_dir()
    downloaded_hashes = set()

    for url in urls:
        fetch_image(url, downloaded_hashes)

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
