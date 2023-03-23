from bs4 import BeautifulSoup
import requests
import smtplib
import time
from simple_colors import *

url_iphone12 = "https://www.olx.com.pk/bahawalnagar_g4060652/mobile-phones_c1453/q-iphone-12"
page_iphone12 = requests.get(url_iphone12)
soup_iphone12 = BeautifulSoup(page_iphone12.content,"html.parser")
iphone12 = soup_iphone12.find_all('article',class_="_7e3920c1")

url_iphone13 = "https://www.olx.com.pk/bahawalnagar_g4060652/mobile-phones_c1453/q-iphone-13"
page_iphone13 = requests.get(url_iphone13)
soup_iphone13 = BeautifulSoup(page_iphone13.content,"html.parser")
iphone13 = soup_iphone13.find_all('article',class_="_7e3920c1")


url_iphone14 = "https://www.olx.com.pk/bahawalnagar_g4060652/mobile-phones_c1453/q-iphone-14"
page_iphone14 = requests.get(url_iphone14)
soup_iphone14 = BeautifulSoup(page_iphone14.content,"html.parser")
iphone14 = soup_iphone14.find_all('article',class_="_7e3920c1")


counter = 0
for i in iphone12:
    counter = counter+1
    name = i.find('div',class_="a5112ca8").text
    price = i.find('span',class_="_95eae7db").text
    iphone12_details = f"{counter}: \033[1mPhone Name is: {name}\nPhone Price is:\033[0m {price}\n"
    print(iphone12_details)

for i in iphone13:
    counter = counter+1
    name = i.find('div',class_="a5112ca8").text
    price = i.find('span',class_="_95eae7db").text
    iphone13_details = f"{counter}: \033[1mPhone Name is: {name}\nPhone Price is:\033[0m {price}\n"
    print(iphone13_details)
    
for i in iphone14:
    counter = counter+1
    name = i.find('div',class_="a5112ca8").text
    price = i.find('span',class_="_95eae7db").text
    iphone14_details = f"{counter}: Phone Name is: {name}\nPhone Price is: {price}\n"
    print(iphone14_details)
    
# while True:
#     smt = smtplib.SMTP("smtp.gmail.com",587)
#     smt.ehlo()
#     smt.starttls()
#     smt.login("charmudassir@gmail.com","rsbjooxzdemhwfkg")
#     smt.sendmail("charmudassir@gmail.com","itzmudassir07@gmail.com",f"Subject:Price Alert by TopaGang\n\n {iphone12_details}")
#     time.sleep(5)

    


