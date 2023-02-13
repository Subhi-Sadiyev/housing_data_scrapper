from bs4 import BeautifulSoup
import json
import pandas
from scraping_code import bina_scraping

markup = bina_scraping.result

soup = BeautifulSoup(markup, 'html.parser')

pagespace = soup.find_all('td')

item_id = soup.find("span", attrs={ 'class': 'item_id'}).text



def converting_list_to_dict(list):
    result_dict = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return result_dict

item_parameters_dict = converting_list_to_dict(pagespace)

item_parameters_dict['ID']= item_id


item_parameters_list = pandas.DataFrame(list(item_parameters_dict.items()))
print(item_parameters_list)
item_parameters_table = pandas.DataFrame.from_dict(item_parameters_dict.items(), orient="columns")


with open("item3208772_parameters_.txt", "w", encoding="utf8") as f:
    print(item_parameters_table, file=f)






# Python3 program to Convert a
# list to dictionary

#def Convert(lst):
#	res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#	return res_dct
		
# Driver code
#lst = ['a', 1, 'b', 2, 'c', 3]
#print(Convert(lst))

#Python program to print table from dict
#def item_parameters_to_table():
#    for i in item_parameters_dict:
#        print("{}\t{}".format(i,item_parameters_dict[i]))