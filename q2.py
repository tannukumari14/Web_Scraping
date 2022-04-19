from re import A
import requests
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
page=requests.get(url)
# print(page)
page.text
soup=BeautifulSoup(page.text,"html.parser")
soup.find("h1")
soup.find("h1").get_text()
soup.find("title")
soup.find("title").get_text()
a=soup.find("title").get_text()
a
exit()