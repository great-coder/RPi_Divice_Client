__author__ = 'Mohammad Dehghan'

import urllib3
import http.client
import urllib.parse
import time


def is_connected():
    try:
        conn = urllib3.connection_from_url('http://irinn.ir/', timeout=1)
        conn.request('GET', '/')
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


def send_request(base_url, port, relative_url, method, content, token, check=False):
    conn = http.client.HTTPConnection(base_url, port)
    params = urllib.parse.urlencode(content)
    if check:
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    else:
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
                   "Authentication": "Bearer " + token}
    conn.request(method, relative_url, params, headers)
    # # conn.send(content)
    # conn.send(params)
    response = conn.getresponse()
    if response.status != 200:
        r = BaseException
        er = response.status + ": " + response.reason
        r.args.__add__(er)
        raise r
    conn.close()
    return response
