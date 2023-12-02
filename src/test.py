import json
import pandas as pd

# json_data = '{"M": [{"dimension_id": "1", "dimension_name": "Bust", "value": "112cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "120cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "135cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "64cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "45cm"}]}'

# json_data = '{"8": [{"dimension_id": "1", "dimension_name": "Bust", "value": "92cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "82cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "90cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "80cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "44cm"}], "10": [{"dimension_id": "1", "dimension_name": "Bust", "value": "97cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "87cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "95cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "80cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "45cm"}], "12": [{"dimension_id": "1", "dimension_name": "Bust", "value": "102cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "92cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "100cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "81cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "46cm"}], "14": [{"dimension_id": "1", "dimension_name": "Bust", "value": "107cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "97cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "105cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "82cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "47cm"}], "16": [{"dimension_id": "1", "dimension_name": "Bust", "value": "112cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "102cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "110cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "82cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "48cm"}], "18": [{"dimension_id": "1", "dimension_name": "Bust", "value": "117cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "107cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "115cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "83cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "50cm"}], "20": [{"dimension_id": "1", "dimension_name": "Bust", "value": "122cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "112cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "120cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "83cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "51cm"}], "22": [{"dimension_id": "1", "dimension_name": "Bust", "value": "127cm"}, {"dimension_id": "3", "dimension_name": "Waist", "value": "117cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "125cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "84cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "52cm"}]}'

json_data = '{"8": [{"dimension_id": "1", "dimension_name": "Bust", "value": "137cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "131cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "61cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "58cm"}], "10": [{"dimension_id": "1", "dimension_name": "Bust", "value": "142cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "136cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "62cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "60cm"}], "12": [{"dimension_id": "1", "dimension_name": "Bust", "value": "147cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "141cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "63cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "61cm"}], "14": [{"dimension_id": "1", "dimension_name": "Bust", "value": "152cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "146cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "64cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "63cm"}], "16": [{"dimension_id": "1", "dimension_name": "Bust", "value": "157cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "151cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "65cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "64cm"}], "18": [{"dimension_id": "1", "dimension_name": "Bust", "value": "162cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "156cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "66cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "66cm"}], "20": [{"dimension_id": "1", "dimension_name": "Bust", "value": "167cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "161cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "66cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "66cm"}], "22": [{"dimension_id": "1", "dimension_name": "Bust", "value": "172cm"}, {"dimension_id": "5", "dimension_name": "Hip", "value": "166cm"}, {"dimension_id": "7", "dimension_name": "Length - shoulder to hem", "value": "66cm"}, {"dimension_id": "15", "dimension_name": "Sleeve Length - neck to hem", "value": "67cm"}]}'

# parsed_data = json.loads(json_data)

path = 'dataset/tops/garment_measurement/the-flutter-sleeve-top#Denim_meta.txt'
import os
DATAPATH = 'dataset/'
CLOTHINGPATH = os.path.join(DATAPATH, 'tops/')
dirpath = os.path.join(CLOTHINGPATH, 'garment_measurement')

# a function to do the intricate work
def parse_json(filepath):
    with open(filepath, 'r') as f:
        json_data = json.load(f)
        # print(type(json_data))
        if type(json_data) == 'str':
            print(filepath)
            f.close()
            return None
    f.close()

    name = filepath.split('/')[-1].split('.')[0]

    data = []
    for size in list(json_data.keys()):
        dims_data = {} # creating a dictionary for each clothing size, easier to work with
        dims_data['name'] = name
        dims_data['size'] = size

        for dim in json_data[size]:
            dims_data[dim["dimension_name"]] = dim["value"]

        data.append(dims_data)
    
    return data

data = []

filepaths = [os.path.join(dirpath, file) for file in os.listdir(dirpath)]

# print(filepaths)
filepaths = ["dataset/tops/garment_measurement/avola-tunic#Sky_meta.txt"]

for filepath in filepaths:
    # filepath = os.path.join(dirpath, file)
    # print(filepath)

    # try:
    #     data_ = parse_json(filepath)
    # except:
    #     print(filepath)
    # data_ = parse_json(filepath)
    print(filepath)

    with open(filepath, 'r') as f:
        json_data = json.load(f)
    f.close()

    name = filepath.split('/')[-1].split('.')[0]

    data_ = []
    for size in list(json_data.keys()):
        dims_data = {} # creating a dictionary for each clothing size, easier to work with
        dims_data['name'] = name
        dims_data['size'] = size

        for dim in json_data[size]:
            dims_data[dim["dimension_name"]] = dim["value"]

        data_.append(dims_data)

    # break
    if data_ is None:
        continue
    
    for d in data_:
        data.append(d)

df = pd.DataFrame(data, index=None)

print(df)

# with open(path, 'r') as f:
#     parsed_data = json.load(f)
#     print(type(parsed_data))
# f.close()
# # print(list(parsed_data.keys())[0])
# print(parsed_data)
# # Extract file name and size
# file_name = "example_file.txt"  # You can replace this with the actual file name

# # size = list(parsed_data.keys())[0]

# # Extract dimensions
# glob_data = []
# for size in list(parsed_data.keys()):
#     dims_data = {}
#     dims_data["size"] = size
    
#     for dim in parsed_data[size]:
#         dims_data[dim["dimension_name"]] = dim["value"]
    
#     glob_data.append(dims_data)

# # Create dataframe
# df = pd.DataFrame(glob_data)

# print(df)
