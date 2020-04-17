import time
import requests as req
from bs4 import BeautifulSoup

hospitals_data = open('hospitals.csv','w+',encoding='utf8')
n = int(input('no. of page to scrape:   '))


named_tuple = time.localtime() # get struct_time
initial_time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print('scraping {}'.format(initial_time))

base_url = 'https://www.hamrodoctor.com/'


for i in range(1,n+1):
    hospitals_url = base_url+'hospitals/index/page:{}'
    response = req.get(hospitals_url.format(i))
    soup = BeautifulSoup(response.content,'html.parser')

    hospitals_div = soup.find_all('div',class_='tg-directinfo')

    for hospitals in hospitals_div:
        hospital = hospitals.find('h3')
        address = hospitals.find('address')
        contact = hospitals.find('ul',attrs={'class':'tg-contactinfo'})
        contact_list = contact.find_all('li')
        contact = contact_list[len(contact_list)-1]
        link= hospitals.find('a')

        hospital_title = hospital.text
        address = address.text
        phone = contact.text
        
        
        inner_hospital_url = base_url+link['href']
        inner_hospital_url_response = req.get(inner_hospital_url)
        inner_hospital_url_soup = BeautifulSoup(inner_hospital_url_response.content,'html.parser')
        inner_hospital_url_doctors = inner_hospital_url_soup.find_all('div',attrs={'class':"col-md-6 col-doctor-list"})

        for doctors in inner_hospital_url_doctors:
            doctor = doctors.find('div',attrs={'class':"tg-directposthead"})
            doctor_name = doctor.h3.text
            doctor_specialist = doctor.div.text

            # print(doctor_name)
            # print(doctor_specialist)

            hospitals_data.write(hospital_title+','+address+','+phone+','+doctor_name+','+doctor_specialist+','+'\n')
        
        

hospitals_data.close()
named_tuple = time.localtime() # get struct_time
final_time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)


print('scraping finished {}'.format(final_time))


