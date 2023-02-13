import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep


##reading a list of item id's from binaz_az_items_id_half.txt (24045 items)"

#items_list_file = open('binaz_az_items_id_half.txt', 'r')

#reading = items_list_file.read()

#items_list = reading.split(',')





##transforming and reading item id's from txt

import re

txt_filename = "items_yeni_tikili_all.txt"

opening_txt = open(txt_filename, 'r')

reading_txt = opening_txt.read()

pattern = re.compile('id.{10}')

yeni_tikili_items_list = pattern.findall(reading_txt)

final_yeni_tikili_items_list = [s.replace('id":"', '') for s in yeni_tikili_items_list]

#print(final_yeni_tikili_items_list)

#with open("bina_az_yeni_tikili_all_items_id.txt", "a", encoding="utf8") as f:
 #       f.write(str(final_yeni_tikili_items_list))





###sorting ids numerically to get a range

#items_list_num_sorted = sorted(items_list)

#with open("bina_az_ids_numerically_sorted.txt", "a", encoding="utf8") as f:
 #   f.write(str(items_list_num_sorted))






###fetching limited amount of items from bina_az

#URL = 'https://bina.az/items/'

#headers = {
 # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
#}

#for item in range(3000006,3058464):
 #   request = requests.get(URL + str(item) + '/', headers=headers)
  #  soup = BeautifulSoup(request.text, 'html.parser')

   # titles = soup.find('title').text
    
   # print(titles)
   # with open("bina_az_tes.txt", "a", encoding="utf8") as f:
    #    f.write(str(titles))

    #sleep(randint(20,30))






### fetching price and view count of limited amount of items


URL = 'https://bina.az/items/'

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}


for item in final_yeni_tikili_items_list:
        
        try:
            
            request = requests.get(URL + str(item.replace(" ", "")) + '/', headers=headers)
            soup = BeautifulSoup(request.text, 'html.parser')

            parameters = soup.find(attrs={"class" : "parameters"}).text
            price = soup.find(attrs={"class" : "azn"}).text
            item_info = soup.find(attrs={"class" : "item_info"}).text
            rent_or_sell = soup.find(attrs={"class" : "type"}).text
            address_description = soup.find(attrs={"class" : "map_address"}).text
            address_tag = soup.find(attrs={"class" : "locations"}).text
    

            print(f" {price} + {rent_or_sell} + {item_info} + {parameters} + {address_description} + {address_tag}")
            with open("bina_az_few_items.txt", "a", encoding="utf8") as f:
                f.write( str(price) + 
                str(' - ') + 
                str(rent_or_sell) + 
                str(' - ') + 
                str(item_info) + 
                str(' - ') +
                str(parameters) +
                str(' - ') + 
                str(address_description) +
                str(' - ') +
                str(address_tag) +
                str(' - ')
                 + str('- Bina-az') )

            sleep(randint(20,30))

        except AttributeError:
            pass
            #with open("bina_az_errors.txt", "a", encoding="utf8") as f:
                #f.write("- Item no longer active - bina.az")

                