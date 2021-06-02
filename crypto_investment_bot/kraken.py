# %%
import time
import os
import requests
import urllib.parse
import hashlib
import hmac
import base64
import keys as k

# Read Kraken API key and secret stored in environment variables
api_url = "https://api.kraken.com"
api_key = k.KRAKEN_API_KEY
api_sec = k.KRAKEN_PRIVATE_KEY


def get_kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()
# %%
# Attaches auth headers and returns results of a POST request
def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req

# %%
resp = kraken_request('/0/private/Balance', {
    "nonce": str(int(1000*time.time()))
}, api_key, api_sec)
print(resp.json())  


# %%

# %%
# Construct the request and print the result
resp = kraken_request('/0/private/AddOrder', {
    "nonce": str(int(1000*time.time())),
    "ordertype": "limit",
    "type": "buy",
    "pair": "DOGEUSD",
    "price": 0.3,
}, api_key, api_sec)
print(resp.json())  

# %%
