import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/dp/B08LRDM44F?pf_rd_r=K8XQ0ZA3MM83KJZ5MVSJ&pf_rd_p=537aa79e-9e4a-40b1-920d-f586be06410e'

headers = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

page = requests.get(URL,headers = headers)

#print(page)

soup = BeautifulSoup(page.content,'html.parser')
product_price = soup.find(id = "priceblock_dealprice")

#print(soup.prettify())

if (product_price == None):
    product_price = soup.find(id ="priceblock_dealprice")

#print (product_price)
print(product_price.getText())

