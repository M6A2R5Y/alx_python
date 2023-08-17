#!/usr/bin/python3
import requests
url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)
# Get the response from the URL
print('Body response:')
print(f'\t- type: {type(response.text)}')
print(f'\t- content: {response.text}')