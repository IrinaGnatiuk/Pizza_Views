from bs4 import BeautifulSoup
import requests
from pprint import pprint as pp

url = 'https://riksha.com.ua/category/pizza'
response = requests.get(url)
contents = response.text

soup = BeautifulSoup(contents, 'lxml')
mydivs = soup.find_all("div", {"class": "catalog__list-item"})
keys = ['name', 'price', 'description','image']
pizza_list = []

for row in mydivs:
    name = row.find_all('div', {'class': 'catalog-card__title'})[0]
    price = row.find_all('div', {'class': 'catalog-card__price'})[0]
    description = row.find_all('div', {'class': 'catalog-card__composition'})[0]
    image = row.find_all('div', {'class': 'catalog-card__img-static js-catalog-card__img-static'})[0]
    values = [name.h2.contents[0], int(price.p.contents[0]), description.p.contents[0], image.picture.img.get('data-src')]
    pizza_dict = dict(zip(keys, values))
    pizza_list.append(pizza_dict)
pp(pizza_list)



