
import requests


url = "https://meowmetry-app.dev1.mnt.group/api/sse"

response = requests.get(url, stream=True)

print("Status:", response.status_code)

for line in response.iter_lines():
    print(line)