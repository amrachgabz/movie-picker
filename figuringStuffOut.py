import random
import json

#dict = {"Name": "Interstellar", "Watched": "Done", "Rating": "★★★★½", "Genre": "Sci-Fi, Mind-Bending, Twisty"}
'''def stars_to_numbers(stars):
    s = stars.count("★")
    if "½" in stars:
        s = s + 0.5
    return s

print(stars_to_numbers(dict["Rating"]))'''

'''def split_genre_tags(genrelist):
    L = genrelist.split()
    return L'''

#print(split_genre_tags(dict["Genre"]))

'''def stars_to_numbers(stars):
    s = stars.count("★")
    if "½" in stars:
        s = s + 0.5
    if s == 0:
        return "Not Rated"
    else:
        return s

print(stars_to_numbers(" "))'''

'''def split_genre_tags(genrelist):
    tags = []
    L = genrelist.split(",")
    for i in L:
        i = i.strip()
        if (i != ""):
            tags.append(i)
    return tags

#print(split_genre_tags("Drama, Tragedy, Thriller")) 
#print(split_genre_tags("Drama, , Thriller"))    
print(split_genre_tags(""))'''

'''def empty_order(order):
    if (order == "None"):
        return 0

print(empty_order("None"))

dict = {"Action": 3, "Adventure": 7}
dict.append("Fantasy")
print(dict["Fantasy"])'''

#importing the json file to python
'''f = open("movies.json", "r", encoding = "utf-8")
mov_lst = json.load(f)
#print(mov_lst)


#Umbrella categorisation of genres
umbrella = {"Heavy": ["Action", "Thriller", "Crime", "Drama", "Adventure"],
            "Light": ["Romance", "Comedy", "Musical", "Family"],
            "Escape": ["Science Fiction", "Fantasy", "True Story"]}

genres = ["Action", "Thriller", "Crime", "Drama", "Adventure", "Romance", "Comedy", "Musical",
          "Family", "Science Fiction", "Fantasy", "True Story"]


#Figuring out shuffle and random

#choice = random.choice(list)
#choices = random.sample(list, 3)

roulette_round_1 = random.sample(mov_lst, 3)
random.shuffle(roulette_round_1)
for picks in roulette_round_1:
    print(picks["name"])'''

L1 = [1, 2, 3, 4, 5]
L2 = list(L1)
L2[3] = 7
print(L1)
print(L2)

