import requests
import sys

def main():
    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)
    response = requests.get('https://api.github.com/user', auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print("Your GitHub user id:", user_data['id'])
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    main()

