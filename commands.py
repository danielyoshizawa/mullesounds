import requests
import json

class Commands:

    def __init__(self):
        pass

    def post(self, payload):
        url = "http://localhost:4000/jsonrpc"
        headers = {'content-type': 'application/json'}

        return requests.post(url, data=json.dumps(payload), headers=headers).json()

    def soundList(self):
        payload = {
            "method" : "soundList",
            "params" : [],
            "jsonrpc" : "2.0",
            "id" : 1,
            }
        response = self.post(payload)
        return response["result"]

    def playSound(self, filename):
        payload = {
            "method": "play",
            "params": [filename],
            "jsonrpc": "2.0",
            "id": 2,
            }
        response = self.post(payload)
