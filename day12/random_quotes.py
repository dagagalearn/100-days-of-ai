# Showing random quotes from API
import requests

url = "https://api.quotable.io/random"
response = requests.get(url)
data = response.json()

print(f"Quote: {data['content']} by {data['author']}")
