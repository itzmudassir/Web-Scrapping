from bs4 import BeautifulSoup
import requests
from csv import writer
import time
for i in range(1, 440):
    url = f"https://www.pakwheels.com/used-cars/search/-/ct_lahore/?page={i}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    cars_lahore = soup.find_all('div', class_="col-md-9 grid-style")

    with open("cars.csv", "a", newline="") as f:
        thewriter = writer(f)
        header = ["Name", "Price", "Location", "Update"]
        thewriter.writerow(header)
        counter = 0
        for cars in cars_lahore:
            counter = counter + 1
            name = cars.find("a", class_="car-name ad-detail-path")
            name = name["title"]
            price = cars.find("div", class_="price-details generic-dark-grey").text.replace("\n\n", "").replace("\n", "").replace(" ", "")
            location = cars.find("ul", class_="list-unstyled search-vehicle-info fs13").text.replace("\n", "").replace(" ", "") 
            update = cars.find("div", class_="pull-left dated").text
            scrapped_list = [name, price, location, update]
            thewriter.writerow(scrapped_list)
            # scrapped_data = f"{counter}: Name: {name}\n    Price: {price}\n    Location: {location}\n    Update: {update}\n"
            # print(scrapped_data)