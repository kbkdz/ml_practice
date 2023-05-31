import os
import requests
from bs4 import BeautifulSoup

# Create function to get the URLS

def fetch_image_urls(keyword, limit):
    urls = []
    total_urls = 0
    current_url = 0

    while total_urls < limit:
        # Perform a Google search and extract image URLs
        search_url = f"https://www.google.com/search?q={keyword}&tbm=isch&start={current_url}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        image_tags = soup.find_all("img")

        # Extract the image URLs
        for image_tag in image_tags:
            if total_urls >= limit:
                break
            try:
                image_url = image_tag["src"]
                if image_url.startswith("https://"):
                    urls.append(image_url)
                    total_urls += 1
            except Exception as e:
                print(f"Error fetching image URL: {str(e)}")

        current_url += 20  # Move to the next page of results

    return urls[:limit]

# Create function to download files

def download_images(keyword, limit):
    # Create a directory to store the downloaded images
    if not os.path.exists(f"images\{keyword}"):
        os.makedirs(f"images\{keyword}")

    # Fetch image URLs
    image_urls = fetch_image_urls(keyword, limit)

    # Download the images
    count = 0
    for image_url in image_urls:
        try:
            response = requests.get(image_url)
            file_path = os.path.join(f"images\{keyword}", f"{count+1}.jpg")
            with open(file_path, "wb") as file:
                file.write(response.content)
            count += 1
        except Exception as e:
            print(f"Error downloading image: {str(e)}")

    return count

# Insert phrases and number of images

keywords = ["guitar", "trumpet"]
limit = 200

# Download the images

for word in keywords:
    downloaded_count = download_images(word, limit)
    print(f"Total images downloaded: {downloaded_count}")

# Files have to be later checked manually to get rid of misleading ones
