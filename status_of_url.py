import requests

url = "https://www.w3schools.com/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Website is online")
    else:
        print("Website is down")
except requests.exceptions.RequestException:
    print("could not reach website ")