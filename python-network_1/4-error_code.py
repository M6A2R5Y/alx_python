#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
   url = sys.argv[1]
   response = requests.get(url)

   print(response.text)

   if response.status_code >= 400:
        print(f"Error code: {response.status_code}")