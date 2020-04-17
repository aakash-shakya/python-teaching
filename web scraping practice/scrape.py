import requests as req
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'

response = req.get(url)

soup = BeautifulSoup(response.content,'html.parser')

table_data = soup.find_all('table',id ="main_table_countries_today")
table_head = []
tdata_odd = []

for data in table_data:
    tr = data.find_all('tr th')
    for i in tr:
        header = i.text()
        table_head.append(header)

    td_odd = data.find_all('tbody tr',class_='odd')
    tdata_odd.append(td_odd)


print(table_head)
print(tdata_odd)