import os
import requests
import json

def download(names, urls, download_path, verbose=False):
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    for name, url in zip(urls, names):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            filename = os.path.join(download_path, name+'.png')

            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Downloaded {name}")
        except requests.exceptions.RequestException as e:
            if verbose:
                print(f"Error downloading {name}")
    if verbose:
        print(f"Content downloaded and saved in {download_path}")

def parse_json(filepath, verbose=False):
    with open(filepath, 'r') as f:
        json_data = json.load(f)
    f.close()

    name = filepath.split('/')[-1].split('.')[0]

    try:
        keys = list(json_data.keys())
    except:
        if verbose:
            print(f"Error parsing {filepath.split('/')[-1]}")
        return None
    
    data = []
    for size in keys:
        dims_data = {} # creating a dictionary for each clothing size, easier to work with
        dims_data['name'] = name
        dims_data['size'] = size

        for dim in json_data[size]:
            dims_data[dim["dimension_name"]] = dim["value"]

        data.append(dims_data)

    return data

import pandas as pd
file = '../data/dataset/humans/humans.csv'
download_path = '../data/dataset/humans/images'
df = pd.read_csv(file)

image_names = df.iloc[:, 0].to_list()
image_urls = df.url.to_list()

if not os.path.exists(download_path):
    os.makedirs(download_path)

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