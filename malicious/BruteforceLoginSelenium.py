from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#IMPORT FOLDER OF THE MODULES
import sys
sys.path.insert(0,'/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register')

#MODULES
from EmailMaker import NamesPickRandom
from PasswordMaker import PasswordPickRandom

options = webdriver.ChromeOptions() 
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# driver.set_window_position(2000, 0)
driver.get("https://10.163.10.244/wp-login.php")
driver.implicitly_wait(2)

driver.find_element(by=By.ID, value="user_login").send_keys(NamesPickRandom())
time.sleep(1)
driver.find_element(by=By.ID, value="user_pass").send_keys(PasswordPickRandom())
time.sleep(1)
driver.find_element(by=By.ID, value="wp-submit").click()
time.sleep(1)


driver.quit()
