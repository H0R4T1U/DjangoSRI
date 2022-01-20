from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd


def scrap(website):
    df = pd.DataFrame()
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)


    driver.get(website.url)
    data = {}

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for div in soup.find_all('div', class_=website.container_class):
        for ScrapedClass in website.classes:
            try:
                data[f"{ScrapedClass}"] = div.find('div', class_=ScrapedClass).text
            except:
                data[f"{ScrapedClass}"] = "null"
            df =df.append(data,ignore_index=True)



    df.to_csv(f"static/dataframes/{website.name}.csv", index=False, encoding='utf-8')
    driver.quit()