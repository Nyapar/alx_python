# import requests module
import requests
 
try:
    response = requests.get('https://alu-intranet.hbtn.io/status')
 
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed with status code:{response.status_code}")
    response = requests.get('https://alu-intranet.hbtn.io/status')
 
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
