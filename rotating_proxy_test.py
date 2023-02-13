###This py takes the proxies from txt and sends requests rotating the ip's

import requests
from bs4 import BeautifulSoup

with open("working_proxies.txt", "r") as f:
    working_proxies = f.read().split("\n")

sites = ["https://bina.az/items/3139803"]

counter = 0

for site in sites:
    try:
        print(f"Using the proxy: {working_proxies[counter]}")
        response = requests.get(site, proxies={"https": working_proxies[counter]})
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find('title').text

        print(response.status_code)
        print(titles)
    except:
        print("fail")
    finally:
        counter += 1