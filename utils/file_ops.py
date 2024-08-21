import os
import json
import csv

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


def save_csv(data:list[dict], filename:str):
    file_path = os.path.join(out_dir, filename)

    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    
    fieldnames = ['hash'] + sorted(key for key in all_keys if key != 'hash')

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            for key in fieldnames:
                if key not in item:
                    item[key] = '0.0'
            writer.writerow(item)