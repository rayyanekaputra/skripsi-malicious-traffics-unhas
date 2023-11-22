import time
import warnings
import requests
import json
import sys

from ProxyScraper import CheckProxyGoogle



warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

def CurrentIP():
    '''
    Return dari CurrentIP adalah dictionary (tadinya json)
    dari IP kita saat ini tanpa proxy
    '''
    current_ip_res = requests.get(url= 'https://api64.ipify.org?format=json',timeout=3, verify = False) #tambahkan verifiy = False kalau Self-Signed
    if current_ip_res.status_code == requests.codes.ok:
            cur_ip_res_json = current_ip_res.json()
            if type(cur_ip_res_json) == dict: #karena dia dict berarti sudah bisa dimaini di python
                  return cur_ip_res_json
            else:
                data = json.loads(cur_ip_res_json)
                print(f'data: {data}')
                return data
    else:
        print('website is down')
    

def CheckIfProxySameAsIP():
    '''
    Return dari CheckIfProxySameAsIP adalah dictionary (tadinya json)
    dari IP kita saat ini tanpa proxy
    '''

    #check apakah IP terganti
    cur_ip_res_json = CurrentIP()
    proxy_ip_res_json = cur_ip_res_json

    while proxy_ip_res_json == cur_ip_res_json:
        '''
        Isinya:

        proxy_raw = {
            "http": f"http://<ip>:<port>",  # HTTP proxy
            "https": f"http://<ip>:<port>}"  # HTTPS proxy
        } --> dictionary
        
        proxy_complete = '<ip>:<port>' --> string
        '''
        proxy_raw, proxy_complete = CheckProxyGoogle()

        #ambil port buat dikasihliat
        http_port = proxy_raw['http'].split(':')[-1]
        try:
            print('Checking to IP Checker.. \033[1m[https://api64.ipify.org?format=json]\033[0m')
            proxy_ip_res = requests.get(url= 'https://api64.ipify.org?format=json',proxies=proxy_raw,timeout=3, verify = False) #tambahkan verifiy = False kalau Self-Signed
            if proxy_ip_res.status_code == requests.codes.ok:
                    print('\033[1m[OK]\033[0m')
                    proxy_ip_res_json = proxy_ip_res.json()
                    if type(proxy_ip_res_json) != dict: #karena dia tidak dict berarti harus diconvert di python
                        data = json.loads(proxy_ip_res_json)
                    proxy_ip_res_json['port'] = http_port
                    print(f'\nSUMMARY:\n\033[1mIP KAMU: \033[91m{cur_ip_res_json}\033[0m\n\033[1mIP PROXY: \033[93m{proxy_ip_res_json}\033[0m\n')
                    return (proxy_raw, proxy_complete)
        except Exception as e:
            print(f'Proxy is down: {e} ')
            continue

  

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    CheckIfProxySameAsIP()

    total_elapsed_time = time.time() - start_time  # Calculate total elapsed time
    print(f"Total Elapsed Time for the Script: {total_elapsed_time:.2f} seconds")