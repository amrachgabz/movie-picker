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
umb_pts_dict = {"Heavy": 0, "Light": 0, "Escape": 0}
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
    for n, film in enumerate(roulette_round):
        print(n+1, film["name"])

    #Getting choice per roulette_round
    ch = int(input("\nPick a movie (1/2/3):"))
    film_genre = roulette_round[ch-1]["genre"]              #takes movie and gets its genre
    umb_name = genre_to_umbrella(film_genre, umbrella)      #identifies the umbrella of the genre
    umb_pts_dict[umb_name] = umb_pts_dict[umb_name] + 1     #increments points for that umbrella 

max_val = max(umb_pts_dict.values())
max_umb = []
for k, v in umb_pts_dict.items():
    if v == max_val:
        max_umb.append(k)

print(max_umb)


#To pick tags of each movie
if len(max_umb) == 1:
    tag_rounds = 4
if len(max_umb) == 2:
    tag_rounds = 2

selected_tags = []
for i in max_umb:
    if i == "Heavy":
        umb = available_heavy
    elif i == "Light":
        umb = available_light
    elif i == "Escape":
        umb = available_escape

    for x in range(tag_rounds):
        random.shuffle(umb)

        if umb:
            check_tag = umb.pop()

        print(check_tag["name"])
        for n, j in enumerate(check_tag["tags"]):
            print(n+1, j)

        print("\nChoose all tags you like. Enter 0 if none")
        l = input("\nEnter Tags: ").strip().split(" ")
        for j in l:
            if j == "0":
                break
            else:
                j = int(j)
            if check_tag["tags"][j-1] not in selected_tags:
                selected_tags.append(check_tag["tags"][j-1])
            else:
                continue

print(selected_tags)