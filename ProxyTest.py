from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import undetected_chromedriver as uc
import time

import sys
sys.path.extend(['/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/'])
from ProxyScraper import ProxyCheckerToWeb

def ProxyTester():
    while True:
        PROXY = ProxyCheckerToWeb()
        options = uc.ChromeOptions() 
        options.page_load_strategy = 'eager' #spy pas load langsung na deteksi
        options.add_argument(f'--proxy-server={PROXY}')
        options.add_argument("--ignore-certificate-errors")
        # options.add_argument("--headless")
        print(f'--proxy-server={PROXY}')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(2.5) #Menunggu DOM load
        driver.get("https://whatismyipaddress.com/")
       
        
        try:
            ISP = driver.find_element(by = By.XPATH, value= '//*[@id="fl-post-111"]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/div/p[1]/span[2]') 
            print("Checking jika ISP berubah..")
            if ISP.text.strip() != "Universitas Hasanuddin":
                print("\nISP Berubah[v]\nProxy Berhasil!")
                driver.quit()
                return PROXY
            else:
                print("\nISP Tetap[x]\nProxy Gagal!")
            driver.quit()

        except WebDriverException as e:
            if "ERR_CONNECTION_RESET" in str(e):
                print("Connection Reset, mencari proxy baru\n")
            elif "ERR_CONNECTION_TIMED_OUT" in str(e):
                print("Connection Timed Out, mencari proxy baru\n")
            elif "ERR_TIMED_OUT" in str(e):
                print("Client Timed Out, mencari proxy baru\n")
            elif "ERR_CONNECTION_CLOSED" in str(e):
                print("Connection Closed, mencari proxy baru\n")
            elif "ERR_PROXY_CONNECTION_FAILED" in str(e):
                print("Proxy Connection Failed, mencari proxy baru\n")
            driver.quit()  # Quit the current WebDriver instance
            continue  # Continue to the next iteration of the loop

        except NoSuchElementException as e:
            print("Error tidak na dapatki elementnya")
            print("\n" + str(e))
            driver.quit()
            continue
        
        
ProxyTester()