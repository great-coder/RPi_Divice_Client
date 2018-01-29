import urllib3
import time


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
        else:
            print("Connection failed!")
            print("Trying again...")
            print('Waiting for %d seconds...' % time_span)
        time.sleep(time_span)
        times -= 1
    if times == 0:
        raise ConnectionError


def send_request(base_url, relative_url, method, content):
    print("request info:\
        base url: " + base_url + "\
        relative url: " + relative_url + "\
        method: " + method + "\
        content: " + content)
