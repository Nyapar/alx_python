#!/usr/bin/python3
import requests
import sys

def get_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK (200)
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            return request_id
        else:
            return "X-Request-Id not found in the response header"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: ./get_request_id.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)
    print("X-Request-Id:", request_id)

