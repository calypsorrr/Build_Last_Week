import time
import requests

username = 'calypsorrr'
feed_name = 'water'
aio_key = ''
url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'

def sendDataWifi(data):
    body = {'value': str(data)}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
        time.sleep(5)
    except Exception as e:
        print(e)
