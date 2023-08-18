#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = input("Enter the URL: ")
    email = input("Enter the email: ")

    data = {'email': email}
    response = requests.post(url, data=data)

    print(response.text)
