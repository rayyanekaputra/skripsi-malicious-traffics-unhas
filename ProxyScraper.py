import requests
from bs4 import BeautifulSoup

#https://realpython.com/beautiful-soup-web-scraper-python/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

URL = "https://www.sslproxies.org/#services"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("div", class_="fpl-list")

for job_element in job_elements:
    print(job_element, end="\n"*2)

# print(job_elements.prettify())