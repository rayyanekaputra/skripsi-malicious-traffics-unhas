import requests
from bs4 import BeautifulSoup
import warnings
import random
#https://realpython.com/beautiful-soup-web-scraper-python/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def ProxyScrape():

    URL = "https://www.sslproxies.org/"
    # URL = "https://free-proxy-list.net/"
    
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
            if columns[1].text.strip() not in ['80', '8080']: #.text karena mau ambil isi text-nya, bukan get_text() --> .text itu 'str'
                # print(columns[1])
                proxy_ip.append(columns[0].text.strip())
                proxy_port.append(columns[1].text.strip())
                proxy_complete.append(columns[0].text.strip() + ":" + columns[1].text.strip()) # Index 2 represents the third column (0-based index)

    # print(type(columns[1].text)) #keluarannya 'str'
    # print(type(proxy_ip), type(proxy_port), type(proxy_complete))
    return (proxy_ip, proxy_port, proxy_complete)

def ProxyCheckerToWeb():
    ProxyScrape()
    proxy_ip, proxy_port, proxy_complete = ProxyScrape()
    while True:

        proxy_rand = random.choice(proxy_complete)
        print(f"\nPROXY SEDANG DICOBA: {proxy_rand} --> ")
        proxy = {
            "http": f"http://{proxy_rand}",  # HTTP proxy
            "https": f"http://{proxy_rand}"  # HTTPS proxy, jangan ganti jadi http:// ke https:// biarkan SSL yang anusendiri
        }
        warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
        # url = "https://103.185.193.35/"
        url = "https://www.google.com/"

        # Check the response
        try:
            response = requests.get(url, proxies=proxy,timeout=3, verify = False) #tambahkan verifiy = False kalau Self-Signed
            print("Proxy dan Request Website Berhasil!\n")

            #check https://requests.readthedocs.io/en/latest/user/quickstart/#response-content
            if response.status_code == requests.codes.ok:
                print (f"== PROXY TERSEDIA: {proxy['http']} ==")
            else:
                response.raise_for_status()  # Raise an exception if the response status is not 200
            return (proxy, proxy_rand)

        except requests.exceptions.RequestException as e:
            print("Google.com --> ")
            print("[REQUEST REFUSED]")

        except requests.exceptions.Timeout as e:
            print("Google.com --> ")
            print("[REQUEST TIMED-OUT]")

        except requests.exceptions.HTTPError as e:
            print("Google.com --> ")
            print("[HTTP ERROR]")

        except requests.exceptions.ConnectionError as e:
            print("Google.com --> ")
            print("[CONNECTION ERROR]")

        except requests.exceptions.TooManyRedirects as e:
            print("Google.com --> ")
            print("[TOO MANY REDIRECTS]")

        except requests.exceptions.MissingSchema as e:
            print("Google.com --> ")
            print("[MISSING SCHEMA]")

        except requests.exceptions.InvalidSchema as e:
            print("Google.com --> ")
            print("[INVALID SCHEMA]")

        except requests.exceptions.InvalidURL as e:
            print("Google.com --> ")
            print("[INVALID URL]")

        except requests.exceptions.InvalidHeader as e:
            print("Google.com --> ")
            print("[INVALID HEADER]")

        except requests.exceptions.InvalidProxyURL as e:
            print("Google.com --> ")
            print("[INVALID PROXY URL]")

        except requests.exceptions.ChunkedEncodingError as e:
            print("Google.com --> ")
            print("[CHUNKED ENCODING ERROR]")

        except requests.exceptions.ContentDecodingError as e:
            print("Google.com --> ")
            print("[CONTENT DECODING ERROR]")

        except requests.exceptions.StreamConsumedError as e:
            print("Google.com --> ")
            print("[STREAM CONSUMED ERROR]")

        except requests.exceptions.RetryError as e:
            print("Google.com --> ")
            print("[RETRY ERROR]")

        except requests.exceptions.UnrewindableBodyError as e:
            print("Google.com --> ")
            print("[UNREWINDABLE BODY ERROR]")

        except Exception as e:
            print(f"Google.com --> An unexpected error occurred: {e}")
