import threading
import queue
import requests

###this py check the https ip's from proxy_list and prints the working ones

q = queue.Queue()
valid_proxies = []

with open("proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


def checking_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            response = requests.get("https://ipinfo.io/json",
            proxies={"https": proxy})
        except:
            #print("not working")
            continue
        if response.status_code == 200:
            print(proxy)
            #with open("working_proxies.txt", "a", encoding="utf8") as f:
                #f.write(proxy + "\n")

for i in range(10):
    threading.Thread(target=checking_proxies).start()
        
