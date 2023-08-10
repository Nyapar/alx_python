import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <letter>")
        return

    letter = sys.argv[1]
    payload = {'q': letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()

