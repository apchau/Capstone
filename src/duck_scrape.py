from selenium import webdriver
import platform
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json
#from pymongo import MongoClient

driver = webdriver.PhantomJS()
# client = MongoClient()
# db = client.test_database
# chemicals_db = db.chemicals
driver.set_window_size(1120, 550)
driver.get("https://www.osha.gov/chemicaldata/")

soup = BeautifulSoup(driver.page_source, "html.parser")
link_list = soup.find_all('a', {'class': 'reportLink'})

final_list = []

for a in soup.find_all('a', {'class': 'reportLink'}, href = True):
    final_list.append(a['href'])

final_list_of_dicts = []
for chemical_link in final_list:
    driver.get('https://www.osha.gov/chemicaldata/' + chemical_link)
    soup_new = BeautifulSoup(driver.page_source, 'html.parser')
    one_chem = soup_new.find_all('tr')
    chemical_dict = {}
    chem_list = []
    i = 0
    for tr in one_chem:
        cols = tr.find_all('td')
        for td in cols:
            if i % 2 == 0:
                chem_list.append(td.text.strip())
            if i % 2 == 1:
                chem_list.append(td.text.strip())
        i += 1

    for j in range(len(chem_list)):
        if j % 2 == 0:
            chemical_dict[chem_list[j]] = chem_list[j+1]
        if j == 39:
            break
    final_list_of_dicts.append(chemical_dict)

with open('chemicals', 'w') as fout:
    json.dump(final_list_of_dicts, fout)

# results = chemicals_db.insert_many(final_list_of_dicts)

# print chemical_dict
# for chemical_link in final_list:
#     driver.get('https://www.osha.gov/chemicaldata/' + chemical_link)
#     soup_new = BeautifulSoup(driver.page_source, 'html.parser')
#
#     chemical_rows = soup.find_all('tr')
#     print chemical_rows
