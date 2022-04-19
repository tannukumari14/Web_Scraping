import json
from task1 import scrap_top_list
from task2 import group_by_year
import json
           
dec_arg=group_by_year(scrap_top_list())

def group_by_decade(movies):
    moviedec={}
    list_1=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list_1:
            list_1.append(decade)
    list_1.sort()

    for i in list_1:
        moviedec[i]=[]
   
    for i in moviedec:
        dec10=int(i)+9
        for x in movies:
            if int(x) <=dec10 and int(x)>=i:
                for v in movies[x]:
                    moviedec[i].append(v)

           
    with open("task_3.json","w") as f:
        json.dump(moviedec,f,indent=6)
    return(moviedec)
print(group_by_decade(dec_arg)) 

