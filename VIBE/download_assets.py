import os
import json
import numpy as np
import pandas as pd
import requests

DATAPATH = 'dataset/'
MODELPATH = os.path.join(DATAPATH, 'humans/')
TOPSPATH = os.path.join(DATAPATH, 'tops/')
ONEPIECEPATH = os.path.join(DATAPATH, 'onepiece/')

def download_humans():
    humans = pd.read_csv(os.path.join(MODELPATH, 'humans.csv'))

    image_names = humans.iloc[:, 0].to_list()
    image_urls = humans.url.to_list()

    download_path = os.path.join(MODELPATH, 'images')

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for name, url in zip(image_names, image_urls):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            filename = os.path.join(download_path, name + '.png')

            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f'Downloaded {name}.png')

        except requests.exceptions.RequestException as e:
            print(f'Failed to download {name}')

def download_tops():
    directory = os.path.join(TOPSPATH, 'img_url')
    tops_urls = []
    tops_names = []
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            filepath = os.path.join(directory, file)
            tops_names.append(file.split('.')[0])

        with open(filepath, 'r') as f:
            urls = f.readlines()
            tops_urls.extend(urls)
    
    tops_urls = [url.strip() for url in tops_urls]
    
    download_path = os.path.join(TOPSPATH, 'images')

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for name, url in zip(tops_names, tops_urls):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            filename = os.path.join(download_path, name + '.png')

            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f'Downloaded {name}.png')

        except requests.exceptions.RequestException as e:
            print(f'Failed to download {name}')

def download_onepiece():
    directory = os.path.join(ONEPIECEPATH, 'img_url')
    onepiece_urls = []
    onepiece_names = []
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            filepath = os.path.join(directory, file)
            onepiece_names.append(file.split('.')[0])

        with open(filepath, 'r') as f:
            urls = f.readlines()
            onepiece_urls.extend(urls)
    
    onepiece_urls = [url.strip() for url in onepiece_urls]
    
    download_path = os.path.join(ONEPIECEPATH, 'images')

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for name, url in zip(onepiece_names, onepiece_urls):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            filename = os.path.join(download_path, name + '.png')

            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f'Downloaded {name}.png')

        except requests.exceptions.RequestException as e:
            print(f'Failed to download {name}')

def main():
    download_humans()
    # download_onepiece()
    # download_tops()

if __name__ == "__main__":
    main()