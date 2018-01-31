__author__ = 'Mohammad Dehghan'

import urllib3
import http.client, urllib.parse
import time
from data.secrets import read_token


def is_connected():
    try:
        conn = urllib3.connection_from_url('http://irinn.ir/', timeout=1)
        r = conn.request('GET', '/')
        return True
    except:
        return False


def connectivity(times, time_span):
    print("Checking network connectivity...")
    while times > 0:
        result = is_connected()
        if result:
            print("Connected successfully!")
            break
        times -= 1
        print("Connection failed!")
        print("Trying again for %d times..." % times)
        print('Waiting for %d seconds...' % time_span)
        time.sleep(time_span)
    if times == 0:
        raise ConnectionError


def send_request(base_url, relative_url, port, method, content):
    print("request info:\nbase_url: " + base_url + "\
        relative_url: " + relative_url + "\
        port: " + port + "\
        method: " + method + "\
        content: " + content)
    conn = None
    try:
        # TODO: Receive content as a Dictionary<string,string> type
        ########################################################################################
        params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
        ########################################################################################
        token = read_token()
        tk_str = "Bearer " + token[0]
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
                   "Authentication": tk_str}
        conn = http.client.HTTPSConnection(base_url, port)
        conn.send(content)
        conn.request(method, relative_url, params, headers)
        response = conn.getresponse()
        if response.status != 200:
            r = BaseException
            er = response.status + ": " + response.reason
            r.args.__add__(er)
            raise r
        return response
    finally:
        print('Closing connection...')
        conn.close()
