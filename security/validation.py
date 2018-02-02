import datetime
from data import secrets
from helpers import date_converter


def token_validation():
    if secrets.file_checker():
        data = secrets.read_token()
        token_date = date_converter.string_to_date(data['token_time'])
        # date format is yyyy/mm/dd
        current_date = datetime.date.today()
        diff = current_date - token_date
        if diff.days < 2:
            return True
        return False
    else:
        return False
