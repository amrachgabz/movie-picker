#Stage 2: python version of the picker app
import json
import random

#importing the json file to python
f = open("movies.json", "r", encoding = "utf-8")
mov_lst = json.load(f)
#print(mov_lst)


#Umbrella categorisation of genres
umbrella = {"Heavy": ["Action", "Thriller", "Crime", "Drama", "Adventure"],
            "Light": ["Romance", "Comedy", "Musical", "Family"],
            "Escape": ["Science Fiction", "Fantasy", "True Story"]}

genres = ["Action", "Thriller", "Crime", "Drama", "Adventure", "Romance", "Comedy", "Musical",
          "Family", "Science Fiction", "Fantasy", "True Story"]


#function to run a genre and find out which umbrella category it falls in
def genre_to_umbrella(genre, umbrella):
    for category in umbrella:
        if genre in umbrella[category]:
            return category
    return None


#Sorting through the json file and finding only the 4+ star rated movies
roulette = []
for mov in mov_lst:
    if mov["rating"] == None:
        continue
    elif mov["watched"] and mov["rating"] >= 4:
        roulette.append(mov)


#Count of how many movies are there in each genre
genre_count = {}
count = 0
for mov in mov_lst:
    if mov["genre"] == "":
        continue
    else:
        if mov["genre"] not in genre_count:
            genre_count[mov["genre"]] = 1
        elif mov["genre"] in genre_count:
            genre_count[mov["genre"]] = genre_count[mov["genre"]] + 1

#for i in genre_count:
    #print(i, ":", genre_count[i])


#Sorting movies into their umbrella categories
heavy = []
light = []
escape = []
for mov in roulette:
    if genre_to_umbrella(mov["genre"], umbrella) == "Heavy":
        heavy.append(mov)
    elif genre_to_umbrella(mov["genre"], umbrella) == "Light":
        light.append(mov)
    elif genre_to_umbrella(mov["genre"], umbrella) == "Escape":
        escape.append(mov)
    else:
        continue


#Picking random movies from each umbrella
'''used = []
for i in range(5):
    roulette_round = []
    for j in range(3):
        if j == 0:
            umb = heavy
        elif j == 1:
            umb = light
        elif j == 2:
            umb = escape

        available = []
        for k in umb:
            if k not in used:
                available.append(k)

        choice = 

        choice = random.choice(umb)
        while choice in used:
            choice = random.choice(umb)
        roulette_round.append(choice)
        used.append(choice)

    print("\nRoulette Round", i+1)
    random.shuffle(roulette_round)
    for film in roulette_round:
        print(film["name"])'''


available_heavy = list(heavy)
available_light = list(light)
available_escape = list(escape)
used = []
for i in range(5):
    roulette_round = []
    for j in range(3):
        if j == 0:
            umb = available_heavy
        elif j == 1:
            umb = available_light
        elif j == 2:
            umb = available_escape

        random.shuffle(umb)
        if umb:
            choice = umb.pop()
            roulette_round.append(choice)
            used.append(choice)

    print("\nRoulette Round", i+1)
    random.shuffle(roulette_round)
    for film in roulette_round:
        print(film["name"])