import requests

url = "https://www.myscheme.gov.in/schemes/pm-kisan"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(response.text[:2000])