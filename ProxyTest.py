from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
        options.add_argument(f'--proxy-server={PROXY}')
        options.add_argument("--ignore-certificate-errors")
        print(f'--proxy-server={PROXY}')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(1) #Menunggu DOM load
        driver.get("https://whatismyipaddress.com/")
       
        
        try:
            ISP = driver.find_element(by = By.XPATH, value= '//*[@id="fl-post-111"]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/div/p[1]/span[2]') 
        except NoSuchElementException:
            print("IP Checker Website is Unreachable")
            
        print("Checking jika ISP berubah..")
        if ISP.text.strip() != "Universitas Hasanuddin":
            print("\nISP Berubah[v]\nProxy Berhasil!")
            driver.quit()
            return PROXY
        else:
            print("\nISP Tetap[x]\nProxy Gagal!")
            driver.quit()
