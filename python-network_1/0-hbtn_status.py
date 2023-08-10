import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print("Error:", response.status_code)

