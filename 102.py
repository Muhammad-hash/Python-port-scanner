#!/bin/python3

#Importing
print("Importing is Important")

import sys #system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())

def new_line():
        print("\n")
        
new_line()

#Advanced strings
print("Advanced Strings:")
my_name = "Heath"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])
print(sentence[-9:]) #last word

print(sentence.split()) #split sentence by delimetre (space)
sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print(sentence_join)
print("\n".join(sentence_split))

qouteception = "I said, 'give me all the mone'"
print(qouteception)

qouteception = "I said, \"give me all the mone\""
print(qouteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter.upper() in word.upper()) #improved - case sensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "       hello        "
print(too_much_space.strip())
 
full_name = "eath Adams"
print(full_name.replace("eath", "Heath"))
print(full_name.find("Adams"))

movie ="The Hangover"
print("My favourite movie is {}.".format(movie))

def favourite_book(tittle,author): #using placeholders
         fav = "My favourite book is \"{}\", which is written by {}.".format(tittle,author)
         return fav
print(favourite_book("The Great Gatsby","F. Scott fitzgerald"))

new_line()

#Dictionaries
print("Dictionaries are keys and values")
drinks = {"White Russian": 7, "Old Fashion" : 10, "Lemon Drop" : 8, "Butterfly Nipple" : 6} #Drink is Key and Price is Value
print(drinks)
new_line()
employees = {"Finance" : {"bob", "linda", "Tina"}, "IT" : {"Gene", "Louise", "Teddy"}, "HR" : {"Jimmy jr ", "Mort"}}
print(employees)

employees ["Legal"] = "Mr Frond" #add new key: value pair
print(employees)

employees.update({"sales" : ["Andie", "Ollie"]})
print(employees)

drinks ["White Russian"] = 8
print(drinks)
print(drinks.get("White Russian"))

#List and Directionaries
movies = ["When Harry Met Sally","The Hangover","The Perks of Being a Wallflower","The Exorcist"]
person = ["Heath", "Jake", "Leah", "Jeff"]

combined = zip(movies,person)
movie_dictionary = {key: value for key, value in combined}
print(movie_dictionary)

































