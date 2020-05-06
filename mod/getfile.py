import json
import os
import sys
from postcodes_io_api import Api

basedir = os.path.abspath('coding-test/stores.json')


def process_jsonfile():
    """
    function get the stores.json from the base directory sort
    names in aphebtical order

    """
    if os.path.isfile(basedir):
        loadstore = open(basedir)
        stores = json.load(loadstore)
        newlist = sorted(stores, key=lambda k: k['name'])
        long_lat = add_lat_long_to_store(newlist)
    return long_lat


def add_lat_long_to_store(sorted_store_list):
    """
    function return valid stores json with longitude and latitude added

    :param json list of stores

    :return - json list of stores with added long and lat
    """
    api = Api()
    new_store_list = []
    for index in sorted_store_list:
        if api.is_postcode_valid(index['postcode']):
            data = api.get_postcode(index['postcode'])
            newdict = {'lat': data['result']['latitude'],
                       'long': data['result']['longitude']}
            index.update(newdict)
            new_store_list.append(index)
    return new_store_list


def get_just_stores():
    """
        function  retrun the name of all stores
        with a valid poscode from the json file
    """
    api = Api()
    string_stores = []
    try:
        if os.path.isfile(basedir):
            loadstore = open(basedir)
            stores = json.load(loadstore)
            sorted_store_list = sorted(stores, key=lambda k: k['name'])
            for index in sorted_store_list:
                if api.is_postcode_valid(index['postcode']):
                    string_stores.append(index['name'])
            return string_stores
    except OSError:
        print("Error cannot open {},\
             please check the file path".format(basedir))
