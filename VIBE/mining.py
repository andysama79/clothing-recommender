import os
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np


# Generate vocabulary from a folder of text files
def generate_vocabulary(folder_path):
    vocabulary = set()
    stop_words = set(stopwords.words('english'))

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                description = file.read()
                tokens = word_tokenize(description.lower())
                tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
                vocabulary.update(tokens)

    return vocabulary

def bin_array(folder_path, vocabulary):
    binary_arrays = []
    i = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            i += 1
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                description = file.read()
                tokens = word_tokenize(description.lower())
                binary_array = [1 if attr in tokens else 0 for attr in vocabulary]
                binary_arrays.append(binary_array)
    print(i)

    return binary_arrays


# Example usage
folder_path = '/home/consularparadi/Downloads/MLPR/clothing-recommender/data/dataset/tops/meta_descriptions'
vocabulary = generate_vocabulary(folder_path)
print(vocabulary.__len__())
print(vocabulary)
binary_arrays = bin_array(folder_path, vocabulary)
print(len(binary_arrays))
binary_arrays = np.array(binary_arrays)
print(binary_arrays.shape)