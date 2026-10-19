import json

f = open("movies.json", "r", encoding = "utf-8")
mov_lst = json.load(f)
print(mov_lst)
#for mov in mov_lst:
    #print(mov)