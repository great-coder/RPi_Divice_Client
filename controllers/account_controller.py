from services.net import send_request


def login():
    print("login")
    send_request("http://localhost:51130", "/oauth", "POST", "grant_type=password&username=username&password=password")
