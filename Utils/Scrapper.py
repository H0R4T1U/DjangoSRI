from django.conf import settings as django_settings
import os


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def scrap(website):
    df = pd.DataFrame()


    driver = webdriver.Firefox()

    driver.get('https://www.pcgarage.ro/notebook-laptop/')
    data = {}

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for div in soup.find_all('div', class_=website.container_class):
        for ScrapedClass in website.classes:
            data[f"{ScrapedClass}"] = div.find('div', class_=ScrapedClass).text
            df =df.append(data,ignore_index=True)



    df.to_csv(f"static/dataframes/{website.name}.csv", index=False, encoding='utf-8')