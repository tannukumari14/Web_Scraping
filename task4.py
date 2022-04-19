from bs4 import BeautifulSoup
import requests
import json

def details_movie(movie_url):
    movie_details = []
    movie_dic = {}
    page = requests.get(movie_url)
   
    soup = BeautifulSoup(page.text,'html.parser')
   
    movie_dic['name'] = 'BlackPanther'
   
    title = soup.find_all('div',class_='meta-label subtle')
    value = soup.find_all('div',class_='meta-value')
   
    for i in range(len(title)):
        movie_dic[str(title[i].get_text().strip())[:-1]] = value[i].get_text().replace(" ","").strip().replace("\n","")
    movie_details.append(movie_dic)

    with open('Task_4.json','w') as file:
        json.dump(movie_details,file,indent=4)

details_movie("https://www.rottentomatoes.com/m/black_panther_")