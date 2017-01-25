import json
from pprint import pprint


def read_json(value):
    print('---------------------------', value, '----------------------------------- ')
    with open(value) as data:
        data = json.load(data)
        pprint(data)

if __name__ == '__main__':

    pprint('-------------------------------map.json---------------------------------')
    with open('map.json') as data_map:
        data_map = json.load(data_map)
    pprint(data_map)

    read_json(data_map['0'])
    read_json(data_map['1'])
    read_json(data_map['2'])
    read_json(data_map['3'])
    read_json(data_map['4'])
    read_json(data_map['5'])
    read_json(data_map['6'])
    read_json(data_map['7'])
    read_json(data_map['8'])
    read_json(data_map['9'])
    read_json(data_map['10'])
    read_json(data_map['11'])
    read_json(data_map['12'])
    read_json(data_map['13'])
    read_json(data_map['14'])
    read_json(data_map['15'])
    read_json(data_map['16'])
    read_json(data_map['17'])
    read_json(data_map['18'])
    read_json(data_map['19'])
    read_json(data_map['20'])
    read_json(data_map['21'])
    read_json(data_map['22'])
    read_json(data_map['23'])
    read_json(data_map['24'])
    read_json(data_map['25'])
    read_json(data_map['26'])
    read_json(data_map['27'])
    read_json(data_map['28'])
    read_json(data_map['29'])
    read_json(data_map['30'])
    read_json(data_map['31'])
    read_json(data_map['32'])
    read_json(data_map['33'])
    read_json(data_map['34'])
    read_json(data_map['35'])
