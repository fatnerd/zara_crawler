import datetime
import requests
import os

class Notify():
    def __init__(self,token):
        self.token = token
        self.api = 'https://notify-api.line.me/api/notify'
    
    def send(self,message):
        headers = {
            "Authorization": "Bearer " + self.token,
        }
        params = {'message':message}
        r = requests.post(self.api,headers = headers,params= params)
        return r.status_code


