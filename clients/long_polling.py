import requests

url = "https://meowmetry-app.dev1.mnt.group/api/poll"

while True:
    try:
        response = requests.get(url, timeout=2)

        print("Status:", response.status_code)
        print("Response:", response.text)
    except requests.Timeout:
        print("Request timed out")
        break
    