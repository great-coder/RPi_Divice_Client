from datetime import datetime
from data import secrets
from helpers import date_converter


def token_validation():
    if secrets.file_checker():
        data = secrets.read_token()
        date = date_converter.string_to_date(data[1])
        # TODO: Check token date validation
        return True
    else:
        return False
