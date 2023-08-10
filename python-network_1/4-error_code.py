import requests
import sys

def get_github_user_id(username, pat):
    try:
        url = "https://api.github.com/user"
        response = requests.get(url, auth=(username, pat))

        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info.get('id')
            if user_id:
                print("GitHub User ID:", user_id)
            else:
                print("User ID not found in the response")
        else:
            print("Error:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: ./github_user_id.py <Nyapar> <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>")
        sys.exit(1)

    username = sys.argv[1]
    pat = sys.argv[2]

    get_github_user_id(Nyapar, pat)
