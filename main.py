from bs4 import BeautifulSoup
import requests


# 下载网页
url = "https://classes.usc.edu/term-20201/classes/csci/"
response = requests.get(url)
response.encoding = response.apparent_encoding

# BeautifulSoup解析网页
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("div", {"id": "CSCI-102"})
print(title.attrs)

#print (soup.prettify())