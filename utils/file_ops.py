import os
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
out_dir = os.path.join(base_dir, "out")

def load_json(filename):
    file_path = os.path.join(data_dir, filename)
    with open(file_path) as jsonfile:
        return json.load(jsonfile)

def save_json(data, filename):
    file_path = os.path.join(out_dir, filename)
    with open(file_path, "w+") as jsonfile:
        json.dump(data, jsonfile)
