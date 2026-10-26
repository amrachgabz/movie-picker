#Stage 2: python version of the picker app
import json

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
        if genre in category:
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

for i in genre_count:
    print(i, ":", genre_count[i])