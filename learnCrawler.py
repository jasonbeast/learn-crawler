# -!- coding: utf-8 -!-  
import requests;
from bs4 import BeautifulSoup;
import json;


for page in range(30):
    page = str(page)
    url="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=ssd&page="+page+"&sort=sale/dc";
    res = requests.get(url);
    data = json.loads(res.text);
    dataProds = data['prods'];
# dataName = data['prods']['name'];
# print(dataProds);
# # print(dataName);
#     print(data['prods']);
    for products in dataProds:
        print(products['name']);
        print(products['price']);