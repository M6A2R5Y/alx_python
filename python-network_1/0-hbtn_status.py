#!/usr/bin/python3
import requests
Url = "https://alu-intranet.hbtn.io/status"
response = requests.get(Url)
# Get the response from the URL
print('Body response:')
print(f'\t- type: {type(response.text)}')
print(f'\t- content: {response.text}')