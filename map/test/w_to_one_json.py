"""
This module save information in one json file.
"""
import json
data_map = {}


def read_map_json():
    with open('C:/workspace/tmp/monopoly/map/map.json') as data_file:
        global data_map
        data_map = json.load(data_file)


def write_chance_item():
    with open('chance.json') as data_file:
        chance_data = json.load(data_file)
        for key, val in chance_data.items():
            with open(val) as data:
                data = json.load(data)
                chance_data[key] = data
                json.dump(chance_data, open("chance.json", "w"), indent=4)


def read_json_for():
    with open('C:/workspace/tmp/monopoly/map/map.json') as data_file:
        dict_map = json.load(data_file)
        for key, val in dict_map.items():
            with open(val) as data:
                data = json.load(data)
                dict_map[key] = data
                json.dump(dict_map, open("overall_json.json", "w"), indent=4)


def read_json_while():
    i = 0
    while i < len(data_map):
        for key, val in data_map.items():
            with open(val) as data:
                data = json.load(data)
                data_map[key] = data
                json.dump(data_map, open("overall_json.json", "w"), indent=4)
                i += 1


if __name__ == '__main__':

    read_map_json()
    print(data_map)
    #write_chance_item()
    #read_json_for()
    read_json_while()
