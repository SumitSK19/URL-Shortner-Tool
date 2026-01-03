import json
import random
import string
import os

DATA_FILE = "urls.json"

def load_urls():
    """Load stored URLs from file if it exists"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_urls(url_data):
    """Save URL mappings to file"""
    with open(DATA_FILE, "w") as file:
        json.dump(url_data, file, indent=4)

def generate_short_code(length=5):
    """Generate a random short code"""
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))

urls = load_urls()

while True:
    print("\n--- URL Shortener ---")
    print("1. Create short URL")
    print("2. Get original URL")
    print("3. Exit")

    user_choice = input("Choose an option: ")

    if user_choice == "1":
        long_url = input("Enter the original URL: ")

        if long_url in urls.values():
            print("This URL has already been shortened.")
        else:
            short_code = generate_short_code()
            urls[short_code] = long_url
            save_urls(urls)
            print(f"Short URL generated: {short_code}")

    elif user_choice == "2":
        short_code = input("Enter the short code: ")

        if short_code in urls:
            print("Original URL:", urls[short_code])
        else:
            print("No URL found for this short code.")

    elif user_choice == "3":
        print("Thank you for using the URL Shortener. Goodbye!")
        break

    else:
        print("Invalid option. Please select 1, 2, or 3.")