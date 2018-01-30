__author__ = 'Mohammad Dehghan'

from services import net
from security import validation


def manage():
    # Check if there is any token from before and check it's expiration, then do login
    if not validation.token_validation():
        login()
    else:
        # TODO: Connect to Chat Hub and broadcast a Hello message! Then go to idle state!!!
        print("Ex-provided token is still valid, use that.")


def login():
    # TODO: Make a request to HomeServer.API to login
    print("login")
    # TODO: Read server(url,port),identity(username,password) and token from secrets.json through secrets.py
    net.send_request("http://localhost:51130", "/oauth", "POST",
                     "grant_type=password&username=username&password=password")
    # secrets.write_token(data)
