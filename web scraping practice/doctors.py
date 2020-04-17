import requests as req
from bs4 import BeautifulSoup

# inner_hospital_url = base_url+link['href']
inner_hospital_url = 'https://www.hamrodoctor.com/hospital/bir-hospital'
inner_hospital_url_response = req.get(inner_hospital_url)
inner_hospital_url_soup = BeautifulSoup(inner_hospital_url_response.content,'html.parser')
inner_hospital_url_doctors = inner_hospital_url_soup.find_all('div',attrs={'class':"col-md-6 col-doctor-list"})

for doctors in inner_hospital_url_doctors:
    doctor= doctors.find('div',attrs={'class':"tg-directposthead"})
    doctor_name = doctor.h3.text
    doctor_specialist = doctor.div.text

    print(doctor_name)
    print(doctor_specialist)
