import requests
from bs4 import BeautifulSoup
import warnings

#https://realpython.com/beautiful-soup-web-scraper-python/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/


URL = "https://www.sslproxies.org/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find("table", class_="table table-striped table-bordered")

proxy_ip = []
proxy_port = []
proxy_complete = []

# Collecting Ddata
for row in job_elements.tbody.find_all('tr'):
    columns = row.find_all('td') #return: dalam bentuk ResultSet bukan list
    if len(columns) >= 0:
        if columns[1] != '80':
            proxy_ip.append(columns[0].text.strip())
            proxy_port.append(columns[1].text.strip())
            proxy_complete.append(columns[0].text.strip() + ":" + columns[1].text.strip()) # Index 2 represents the third column (0-based index)

# Define the proxy information

while True:
    import random
    proxy_rand = random.choice(proxy_complete)
    print(f"\n PROXY DI PAKE: {proxy_rand} --> ")
    proxy = {
        "http": f"http://{proxy_rand}",  # HTTP proxy
        "https": f"http://{proxy_rand}"  # HTTPS proxy, jangan ganti jadi http:// ke https:// biarkan SSL yang anusendiri
    }
    warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
    url = "https://103.185.193.35/"

    # Check the response
    try:
        response = requests.get(url, proxies=proxy,timeout=3, verify = False) #tambahkan verifiy = False kalau Self-Signed
        print("Proxy dan Request Website Berhasil!")

        response.raise_for_status()  # Raise an exception if the response status is not 200
        break
        
    except requests.exceptions.RequestException as e:
        if "refused" in str(e):
            print("Proxy Gagal [REFUSED]")
        elif isinstance(e, requests.exceptions.Timeout):
            print("Request Website Gagal [REQUEST TIMED OUT]")
        else:
            print(f"Proxy dan Request Gagal: {e}")