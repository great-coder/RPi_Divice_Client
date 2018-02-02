__author__ = 'Mohammad Dehghan'

from services import net
from security import validation
from data import secrets


def manage():
    net.connectivity(20, 5)
    # Check if there is any token from before and check it's expiration, then do login
    if not validation.token_validation():
        login()
    else:
        # TODO: Connect to Chat Hub and broadcast a Hello message! Then go to idle state!!!
        print("Ex-provided token is still valid, use that.")


def login():
    print("Trying to login...")
    server = secrets.read_server()
    identity = secrets.read_identity()
    content = {"grant_type": "password", "username": identity['username'], "password": identity['password']}
    response = net.send_request(server['url'], server['port'], 'oauth', 'POST', content, None, True)
    print(response)
# secrets.write_token(data)
