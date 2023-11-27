import time
import requests
from ping3 import ping

def check_ip_uptime(target_ip, interval=5, max_failures=5, proxy=None):
    failures = 0

    while True:
        result = ping(target_ip)

        if result is not None:
            print(f"{target_ip} is UP (Round-Trip Time: {result} ms)")
            failures = 0
        else:
            print(f"{target_ip} is DOWN")
            failures += 1

            if proxy:
                try:
                    response = requests.get(f"http://{target_ip}", proxies=proxy, timeout=10)
                    if response.status_code == 200:
                        print(f"Proxy ({proxy['https']}) responded with HTTP 200 OK")
                except requests.exceptions.RequestException as e:
                    print(f"Proxy ({proxy['https']}) failed to reach the target: {e}")

        if failures >= max_failures:
            print(f"{target_ip} has been down for too long. Exiting.")
            break

        time.sleep(interval)

if __name__ == "__main__":
    target_ip = "rayyanekaputra.space"  # Replace with the IP address you want to check
    proxy = {
        "http": "socks4://146.190.74.225:41497",
        "https": "socks4://146.190.74.225:41497",
    }  # Replace with your proxy server information if needed

    check_ip_uptime(target_ip, proxy=proxy)
