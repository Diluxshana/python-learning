import requests

url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"

response = requests.get(url)

print(response.text)