from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def scrap(self):
    driver = webdriver.Firefox()
    products = []
    prices = []
    ratings = []
    websites = self.get_all()
    for website in websites:
        driver.get(website.url)

        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        for div in soup.find_all('div', class_=website.container_class):

            name = div.find('div', class_=website.classes[0])
            price = div.find('div', class_=website.classes[1])
            rating = div.find('span', class_=website.classes[2])
            products.append(name.text)
            prices.append(price.text)
            if rating:
                ratings.append(len(list(rating.descendants)))
            else:
                ratings.append(0)

    df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
    df.to_csv('products.csv', index=False, encoding='utf-8')