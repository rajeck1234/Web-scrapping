from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.headless = True
driver = webdriver.Chrome('chromedriver',options=chrome_options)
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source
soup = BeautifulSoup(content)
all_laptops = soup.findAll('div', attrs={'class':'_2kHMtA'})

for laptop1 in all_laptops:
    laptop = soup
    name=laptop.find('div', attrs={'class':'_4rR01T'})
    price=laptop.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=laptop.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text.strip())
    prices.append(price.text.strip())
    ratings.append(rating.text.strip()) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('laptop_details.csv', index=False, encoding='utf-8')
soup.findAll('div', attr = {'class':'_2kHMtA'})
res = soup.findAll('div',{"class":"_4rR01T"})
soup.findAll('div', attr = {'class':'col col-5-12 nlI3QM'})
print(soup.prettify())
