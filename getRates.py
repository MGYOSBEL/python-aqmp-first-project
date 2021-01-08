import json
import requests

apiUrl = "http://pruebatecnica.aquilessolutions.com/rates"

def getRates():
    response = requests.get(apiUrl)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
