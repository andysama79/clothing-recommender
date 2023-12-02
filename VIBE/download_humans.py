import pandas as pd
import os
import requests

file = 'dataset/humans/humans.csv'
download_path = 'dataset/humans/images'
df = pd.read_csv(file)

image_names = df.iloc[:, 0].to_list()
image_urls = df.url.to_list()

for name, url in zip(image_names, image_urls):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        filename = os.path.join(download_path, name+'.jpg')

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Downloaded {name}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {name}")