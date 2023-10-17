from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)

driver.get("https://10.163.10.244/wp-login.php")
driver.implicitly_wait(2)


driver.find_element(by=By.ID, value="user_login").send_keys('resephariankamu')
time.sleep(1)
driver.find_element(by=By.ID, value="user_pass").send_keys('LiG5hqDiMNCacSa')
time.sleep(1)
driver.find_element(by=By.ID, value="wp-submit").click()
time.sleep(1)

driver.quit()