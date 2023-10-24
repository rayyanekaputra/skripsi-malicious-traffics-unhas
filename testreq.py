import time
import requests
from ping3 import ping

proxy = {
        "http": "socks4://51.68.39.222:29302",
        "https": "socks4://51.68.39.222:29302",
        } 

try:
    response = requests.get(f"https://rayyanekaputra.space", proxies=proxy, timeout=10)
    if response.status_code == 200:
        print(f"Proxy ({proxy['https']}) responded with HTTP 200 OK")
except requests.exceptions.RequestException as e:
    print(f"Proxy ({proxy['https']}) failed to reach the target: {e}")