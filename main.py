import requests
import os

# URL of the file to download
url = "http://cicresearch.ca/CICDataset/MalDroid-2020/Dataset/APKs/Riskware.tar.gz"

# Destination file path (adjust as needed)
download_path = "Riskware.tar.gz"

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Send a GET request with headers
    response = requests.get(url, headers=headers, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the destination file in binary write mode
        with open(download_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"File downloaded successfully to {os.path.abspath(download_path)}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")