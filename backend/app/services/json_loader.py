import os
import json


def load_json_data(folder_name, file_name):
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data
