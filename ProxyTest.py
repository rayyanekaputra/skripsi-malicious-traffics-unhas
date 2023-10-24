from selenium import webdriver
import undetected_chromedriver as uc 
import time

PROXY = "171.233.251.114:9090"

options = uc.ChromeOptions() 
options.add_argument(f'--proxy-server={PROXY}')
print(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(options=options)
driver.get("https://whatismyipaddress.com/")
driver.maximize_window() 
time.sleep(10)

driver.quit()
