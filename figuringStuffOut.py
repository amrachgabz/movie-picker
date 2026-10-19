dict = {"Name": "Interstellar", "Watched": "Done", "Rating": "★★★★½", "Genre": "Sci-Fi, Mind-Bending, Twisty"}
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

def empty_order(order):
    if (order == "None"):
        return 0

print(empty_order("None"))

