from selenium import webdriver
import time

PROXY = "35.236.207.242:33333"
options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={PROXY}')
print(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(options=options)
driver.get("https://whatismyipaddress.com/")
time.sleep(1)


driver.quit()
