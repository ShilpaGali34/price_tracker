import requests

from bs4 import BeautifulSoup

#URL = 'https://www.amazon.in/HP-Laptop-14-Inch-Windows-dy2501tu/dp/B093VZC5X9#customerReviews'

URL = 'https://www.amazon.in/Oppo-Mystery-Storage-Additional-Exchange/dp/B08444S68L?ref_=Oct_DLandingS_D_061843d5_60&smid=A14CZOWI0VEHLG'

headers = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

page = requests.get(URL,headers = headers)

#print(page)

soup = BeautifulSoup(page.content,'html.parser')

product_price = soup.find(id = "priceblock_dealprice")

if (product_price == None):
    product_price = soup.find(id="priceblock_ourprice")

#print(soup.prettify())

print(product_price.getText())