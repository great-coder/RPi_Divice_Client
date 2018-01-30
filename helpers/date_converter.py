__author__ = 'Mohammad Dehghan'

import datetime


def date_to_string(date):
    output = date + ""
    return output


def string_to_date(string):
    output = datetime.datetime.strptime(string, "%Y/%m/%d").date()
    return output
