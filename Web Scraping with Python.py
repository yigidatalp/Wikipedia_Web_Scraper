# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:59:07 2023

@author: Yigitalp
"""

# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# set URL
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# set page (whether it's connected or not)
page = requests.get(url)

# convert page to text with HTML format
soup = BeautifulSoup(page.text, 'html')

# get the 1st table's contents (desired table is in position 1)
table1 = soup.find_all('table')[1]

# find the 1st table's titles and create the empty DataFrame with these titles
titles1 = table1.find_all('th')
titles1_list = [title1.text.strip() for title1 in titles1]


# find the 1st table's data and append them into the DataFrame
rows = table1.find_all('tr')
data_list = []
for row in rows[1:]:
    row_data = row.find_all('td')
    data_list.append([data.text.strip() for data in row_data])
        
df = pd.DataFrame(data_list, columns = titles1_list)