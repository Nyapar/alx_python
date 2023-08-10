# import requests module
import requests
 
try:
    # Making a get request to a valid URL
    response = requests.get('https://alu-intranet.hbtn.io/status')
 
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.text)
    else:
        # Print an error message if the request was not successful
        print(f"Request failed with status code: {response.status_code}")
 
    # Making a get request to an incorrect URL
    response = requests.get('https://alu-intranet.hbtn.io/status')
 
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.text)
    else:
        # Print an error message if the request was not successful
        print(f"Request failed with status code: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    # Handle any exceptions that may occur during the request
    print(f"An error occurred: {e}")
