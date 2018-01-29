import json


def validation():
    print("Token validation")
    return False


def token_checker():
    file_name = "token.json"
    access_mode = "r"
    try:
        token_file = open(file_name, access_mode)
        return validation()
    except FileNotFoundError:
        return False


def write(data, file_name):
    # get a string dictionary as input
    with open(file_name, "w") as file:
        json.dump(data, file_name)


def read(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        # return a string dictionary as output
