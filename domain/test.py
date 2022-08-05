import requests

url = "https://pro-cycling-stats.p.rapidapi.com/riders"

headers = {
	"X-RapidAPI-Key": "287b1849d6mshbef2241bd6f3c2ep1673dejsn3436f96261e2",
	"X-RapidAPI-Host": "pro-cycling-stats.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)