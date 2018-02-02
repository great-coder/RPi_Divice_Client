__author__ = 'Mohammad Dehghan'

import json

file_name = "secrets.json"


def file_checker():
    try:
        file = open(file_name, "r")
        file.close()
        return True
    except:
        # secrets.json file doesn't exist
        return False


def read_identity():
    with open(file_name, "r") as file:
        data = json.load(file)
    return data['identity']


def read_token():
    with open(file_name, "r") as file:
        data = json.load(file)
    return data['token']


def read_server():
    with open(file_name, "r") as file:
        data = json.load(file)
    return data['server']


def write_identity(data):
    file = None
    try:
        # TODO: Read previous data from file (if exists), then update data
        file = open(file_name, "w")
        json.dump(data, file)
        output = True
    except:
        output = False
    finally:
        file.close()
    return output


def write_token(data):
    # TODO: get a string dictionary as input, then convert it into json format
    with open(file_name, "w") as file:
        json.dump(data, file)


def write_server(data):
    file = None
    try:
        # TODO: Read previous data from file (if exists), then update data
        file = open(file_name, "w")
        json.dump(data, file)
        output = True
    except:
        output = False
    finally:
        file.close()
    return output
