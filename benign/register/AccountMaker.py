from EmailMaker import EmailPickRandom, NamesPickRandom
from PasswordMaker import PasswordPickRandom

#Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def AccountMaker():
    options = webdriver.ChromeOptions() 
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    # driver.set_window_position(2000, 0)
    driver.get("https://10.163.10.244/wp-login.php")

    driver.find_element(By.XPATH, "//*[@id='nav']/a[1]").click()
    driver.find_element(by=By.ID, value="user_login").send_keys(NamesPickRandom())
    driver.find_element(by=By.ID, value="user_email").send_keys(EmailPickRandom())

    driver.find_element(by=By.ID, value="wp-submit").click()
    time.sleep(1)

    driver.quit()   