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
    output = []
    with open(file_name, "r") as file:
        data = json.load(file)
        for i in data['identity']:
            output[0] = i['username']
            output[1] = i['password']
    return output


def read_token():
    output = []
    with open(file_name, "r") as file:
        data = json.load(file)
        for i in data['token']:
            output[0] = i['access_token']
            output[1] = i['token_time']
    return output


def read_server():
    output = []
    with open(file_name, "r") as file:
        data = json.load(file)
        for i in data['server']:
            output[0] = i['url']
            output[1] = i['port']
    return output


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
