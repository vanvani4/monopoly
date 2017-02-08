"""
This module save information from json files in global variables.
"""
import json

dict_map = {}
sector_id_list = {}
content_sector_id = {}
sector_information = {}


def read_map_json():
    global dict_map
    with open('map.json') as data_file:
        dict_map = json.load(data_file)
        return dict_map


def read_json_for():
    for val in list(dict_map.values()):
        with open(val) as data:
            global sector_information
            sector_information.update(json.load(data))


def read_json_while():
    global sector_id_list
    sector_id_list = list(dict_map.values())
    i = 0
    while i < len(sector_id_list):
        with open(sector_id_list[i]) as data:
            global content_sector_id
            content_sector_id.update(json.load(data))
            i += 1


if __name__ == '__main__':

    read_map_json()
    read_json_for()
    read_json_while()
