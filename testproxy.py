import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
proxy = {
    'http' : 'https://210.230.238.153:443'
}


try:
    response = requests.get(url, proxies=proxy,timeout=3, verify = False)
    response.raise_for_status()  # Raise an exception if the response status is not 200
    print("Request was successful!")
except requests.exceptions.RequestException as e:
    if "refused" in str(e):
        print("Proxy was refused")
    elif isinstance(e, requests.exceptions.Timeout):
        print("Request timed out")
    else:
        print(f"Request failed with an error: {e}")
