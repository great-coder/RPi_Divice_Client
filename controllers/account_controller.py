__author__ = 'Mohammad Dehghan'

from services import net
from security import validation
from data import secrets


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
    server = secrets.read_server()
    identity = secrets.read_identity()
    content = "grant_type=password&username=" + identity[0] + "&password=" + identity[1]
    # TODO: Send content as a Dictionary<string,string> type
    ############################################################################
    response = net.send_request(server[0], '/oauth', server[1], 'POST', content)
    ############################################################################
    print(response)
    # secrets.write_token(data)
