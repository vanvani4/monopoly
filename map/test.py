import json
from pprint import pprint


def read_json(value):
    print('-----------------------', value, '------------------------------- ')
    with open(value) as data:
        data = json.load(data)
        pprint(data)


def read_json_for1():
    with open('map.json') as data_map:
        data_map = json.load(data_map)
        pprint('---------------------------map.json--------------------------')
        pprint(data_map)
    for x in list(data_map.values()):
        print('-----------------------', x, '------------------------------- ')
        with open(x) as data:
            data = json.load(data)
            pprint(data)


def read_json_for2():
    with open('map.json') as data_map:
        data_map = json.load(data_map)
        pprint('---------------------------map.json--------------------------')
    for index, val in enumerate(list(data_map.values())):
        print(index, val)
    for x in list(data_map.values()):
        print('-----------------------', x, '------------------------------- ')
        with open(x) as data:
            data = json.load(data)
            for index, val in enumerate(data.values()):
                print(index, val)


def read_json_while():
    with open('map.json') as data_map:
        data_map = json.load(data_map)
    pprint('---------------------------map.json------------------------------')
    pprint(data_map)
    list_values = list(data_map.values())
    i = 0
    while i < 36:
        print('---------------', list_values[i], '-------------------------- ')
        with open(list_values[i]) as data:
            data = json.load(data)
            pprint(data)
            i += 1


if __name__ == '__main__':
    print('__________________________________________test without cycles___________________________________________')
    pprint('---------------------------map.json------------------------------')
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

    print('__________________________________________test with for cycle___________________________________________')
    read_json_for1()
    print('__________________________________________test with for cycle and index_________________________________')
    read_json_for2()
    print('__________________________________________test with while cycle_________________________________________')
    read_json_while()
