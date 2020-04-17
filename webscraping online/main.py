import requests as req
from bs4 import BeautifulSoup

url = 'https://www.hamrodoctor.com/hospitals/index/page:2'

response = req.get(url)

soup = BeautifulSoup(response.content,'html.parser')

div = soup.find_all('div',attrs={'class':"tg-directinfo"})

for i in div:
    title = i.find('h3')
    div2 = i.find('ul',attrs={'class':'tg-contactinfo'})
    li = div2.find_all('li')
    print(title.text)
    for j in range(len(li)):
        li_text = li[j].text
        print(li_text)
    print('\n')