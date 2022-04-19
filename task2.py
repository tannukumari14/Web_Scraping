import requests
import json
import pprint
from task1 import top_movie_list

def group_by_year(movies):
    years=[]
    for i in movies:
        year=i['year']
        if year not in years:
            years.append(year)
    movies_dict={i:[] for i in years}
    for i in movies:
        year=i['year']
        for x in movies_dict:
            if str(x)==str(year):
                movies_dict[x].append([i])
    with open('task_2.json','w') as file:
        json.dump(movies_dict,file,indent=4)

        return movies_dict
print(group_by_year(top_movie_list))

