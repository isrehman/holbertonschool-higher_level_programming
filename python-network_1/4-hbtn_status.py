#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status using requests"""
import requests


if __name__ == "__main__":
    response = requests.get(
        "https://intranet.hbtn.io/status",
        headers={'cfclearance': 'true'}
    )
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
