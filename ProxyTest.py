import requests
import json
import sys

from ProxyScraper import ProxyCheckerToWeb, ProxyScrape

def ProxyTester():
    
    current_ip_res = requests.get(url= 'https://api64.ipify.org?format=json',timeout=3, verify = False) #tambahkan verifiy = False kalau Self-Signed
    if current_ip_res.status_code == requests.codes.ok:
            cur_ip_res_json = current_ip_res.json()
            if type(cur_ip_res_json) == dict: #karena dia dict berarti sudah bisa dimaini di python
                  print(f'data: {cur_ip_res_json}')
            else:
                data = json.loads(cur_ip_res_json)
                print(f'data: {data}')
    else:
        print('website is down')
    
    #check apakah IP terganti
    proxy_ip_res_json = cur_ip_res_json
    while cur_ip_res_json == proxy_ip_res_json:
        proxy_raw, proxy_complete = ProxyCheckerToWeb()
        print(f'print{proxy_raw}')
        try:
            proxy_ip_res = requests.get(url= 'https://api64.ipify.org?format=json',proxies=proxy_raw,timeout=3, verify = False) #tambahkan verifiy = False kalau Self-Signed
            if proxy_ip_res.status_code == requests.codes.ok:
                    proxy_ip_res_json = proxy_ip_res.json()
                    if type(proxy_ip_res_json) == dict: #karena dia dict berarti sudah bisa dimaini di python
                        print(f'data: {proxy_ip_res_json}')
                    else:
                        data = json.loads(proxy_ip_res_json)
                        print(f'data: {data}')
                    print('DONE')
                    print(proxy_complete)
                    return (proxy_raw, proxy_complete)
        except Exception as e:
            print(f'proxy is down: {e} ')
            continue

    print(f'ip saat ini: {cur_ip_res_json}\nip proxy: {proxy_ip_res_json}')
ProxyTester()