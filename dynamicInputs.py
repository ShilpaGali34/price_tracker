import requests

from bs4 import BeautifulSoup

#URL = 'https://www.amazon.in/dp/B08LRDM44F?pf_rd_r=K8XQ0ZA3MM83KJZ5MVSJ&pf_rd_p=537aa79e-9e4a-40b1-920d-f586be06410e'

headers = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

products_to_track = [
    {
        "URL"  :"https://www.amazon.in/Oppo-Mystery-Storage-Additional-Exchange/dp/B08444S68L?ref_=Oct_DLandingS_D_061843d5_60&smid=A14CZOWI0VEHLG",
        "name" : "OppoA31"
    },
    {
        "URL"  : "https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6/ref=lp_4363159031_1_1",
        "name" : "samsung galaxy m31"
    },
    {
        "URL"  : "https://www.amazon.in/dp/B092QH39Q1/ref=QANav11CTA_en_IN_4?pf_rd_r=KGHMYBTVTXVV64AS4ZXJ&pf_rd_p=3f1b0210-6ac8-43ae-a21c-f7fa984773f0&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-10&pf_rd_t=&pf_rd_i=1389401031",
        "name" : "Realme"
    }
]

def give_product_price(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id ="priceblock_ourprice")
    #print(product_price)
    return product_price.getText()

for every_product in products_to_track:
    product_price_returned = give_product_price(every_product.get("URL"))
    print(product_price_returned + "-" + every_product.get("name"))
