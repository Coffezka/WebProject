from django.test import TestCase
import requests
import json
import os

class AccountMethods(TestCase):
    def testLoginSuccess(self):
        body = {
                'username': 'Durotan@gmail.com',
                'password': 'DurotanDurotan'
            }
        headers = {'content-type': 'application/json'}
        r = requests.post('http://127.0.0.1:8000/api/account/login', data=json.dumps(body),headers=headers)

        print("Test: "+ str(r.json()['token']))
        #print(os.environ['passwordValid'])

        self.assertEqual(r.json()['token'],'ff43c9b0095fed2f19c97c63861af794edd6c1f0')
    def testLoginUnsuccess(self):

        body = {
                'username': 'Durotan1@gmail.com',
                'password': 'DurotanDurotan'
            }
        headers = {'content-type': 'application/json'}
        r = requests.post('http://127.0.0.1:8000/api/account/login', data=json.dumps(body),headers=headers)

        self.assertTrue((str(r.json()['non_field_errors'][0])=='Unable to log in with provided credentials.'))
        

