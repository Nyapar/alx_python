import requests

url = "https://alu-intranet.hbtn.io/status"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the response status is not OK (200)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
