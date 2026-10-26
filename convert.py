#program to convert the csv file into a json file for readability

import csv
import json

f = open("movies.csv", "r", encoding = "utf-8-sig")
reader = csv.DictReader(f)

#Function to convert the stars to numerical values
def stars_to_numbers(stars):
    s = stars.count("★")
    if "½" in stars:
        s = s + 0.5
    if s == 0:
        return None
    else:
        return s

#function to turn a string of words into a list 
def split_tags(taglist):
    tags = []
    L = taglist.split(",")
    for i in L:
        i = i.strip()
        if (i != ""):
            tags.append(i)
    return tags

#functions to handle empty columns
def empty_column(column):
    if (column == ""):
        return None
    else:
        return column

def convert_to_number(column):
    if (column == ""):
        return None
    else:
        return int(column)

#list of dictionaries
movie_list = []
for row in reader:
    movie = {}
    movie["name"] = row["Name"] 
    movie["watched"] = row["Watched"] == "Done" 
    movie["genre"] = row["Genre"].strip()
    movie["tags"] = split_tags(row["Tags"])
    movie["rating"] = stars_to_numbers(row["Rating"])
    movie["series"] = empty_column(row["Series"])
    movie["order"] = convert_to_number(row["Order"])
    movie["year"] = convert_to_number(row["Year"])
    movie_list.append(movie)

f.close()

#Writing everything into a json file
f = open("movies.json", "w", encoding = "utf-8")
json.dump(movie_list, f, indent = 2, ensure_ascii = False)
f.close()