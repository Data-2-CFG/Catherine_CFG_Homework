# -*- coding: utf-8 -*-
"""week_3_homework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WiF9F7SXbWZDOIDqodHX4VL9gbaP_WAy
"""

#  TASK 1 (Conditional flow)

# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

weather  = input('Is it raining ? y/n')
if weather == 'y':
  print('Take an umbrella')
if weather == 'n':
  print("You don't need an umbrella")

# Question 2
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. 
#I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong

my_money = input('How much money do you have? ')
boat_cost = 20 + 5

if my_money < boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire'
### your input should be int or float, your code will break if someone input a string
# Also if you have the 25, you still can afford the boat hire. so I would add my_money <= boat_cost

# Right answer:
my_money = float(input('How much money do you have? '))
boat_cost = 20 + 5

if my_money <= boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire')

# Question 3
# Your friend works for an antique book shop that sells books between 1800 and 1950
#  and wants to quickly categorise books by the century and decade that they were written.
#   Write a program that takes a year (e.g. 1872) and outputs the century and decade
#    (e.g. "Eighteenth Century, Seventies")

age = {'10':'Teens','20':'Twenties','30': 'Thirties','40':'Forties','50':'Fifties','60':'Sixties','70':'Seventies','80':'Eighties','90':'Ninties'}

book = int(input('when was the book published? bewteen 1800-1950'))
if 1800 <=book < 1900:
    book = str(book)
    print(f'Eighteenth Century, {age[book[2:]]}')
if 1900 <= book <= 1950:
    book = str(book)
    print(f'Nineteenth Century, {age[book[2:]]}')

# TASK 2 (Lists and Dictionaries)


# Question 1
# I have a list of things I need to buy from my supermarket of choice.

# shopping_list = [
# 	"oranges",
# 	"cat food",
# 	"sponge cake",
# 	"long-grain rice",
# 	"cheese board",
# ]
# print(shopping_list[1])
 
# I want to know what the first thing I need to buy is. However,
# when I run the program it shows me a different answer to what I was expecting? What is the mistake? How do I fix it.

# Answer :
 # the list index starting with 0, so your code should be 
 print(shopping_list[0])

# Question 2
# # I'm setting up my own market stall to sell chocolates.
#  I need a basic till to check the prices of different chocolates that I sell.
#  I've started the program and included the chocolates and their prices. 
#  Finish the program by asking the user to input an item and then output its price.
 
chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}


## Answer
choc = input('What kind of chocolates would you like to buy? white/milk/dark/vegan')
print(chocolates[choc])

# Question 3
# Write a program that simulates a lottery. 
# The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers. After comparing the two sets of numbers,
# the program should output a prize based on the number of matches:
# ·         £20 for three matching numbers
# ·         £40 for four matching numbers
# ·         £100 for five matching numbers
# ·         £10000 for six matching numbers
# ·         £1000000 for seven matching numbers

import random
your_ticket = [55,60,7,4,95,8,36]   # your lottery ticket

lottery_ticket = []
for i in range(len(your_ticket)):      ## generate a list of random number as winning ticket
  lottery_ticket.append(random.randint(1,99))

counter = 0
for num in your_ticket:
  if num in lottery_ticket:   ### how many numbers are matching
    counter += 1

if counter <= 2:          ### checking prize
  print('you have won nothing')
elif counter == 3:
  print('you have won £20')
elif counter == 4:
  print('you have won £40')
elif counter == 5:
  print('you have won £100')
elif counter == 6:
  print('you have won £10000')
elif counter == 7:
  print('you have won £1000000')

# TASK 3 (Read and Write files)

# Question 1
 
# You're having coffee/tea/beverage of your choice with a friend that is learning to program in Python.
#  They're curious about why they would use pip. Explain what pip is and one benefit of using pip.



# Answer : PIP is a package manager for Python packages, A package contains all the files you need for a module.

# Modules are Python code libraries you can include in your project.
# Benefit : it allows you to install additional libraries and packages that are not part of the standard Python library

# Question 2


# This program should save my data to a file, 
# but it doesn't work when I run it. What is the problem and how do I fix it?
 
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'r') as poem_file:
# 	poem_file.write(poem)

## Answer:
# you have chose 'read' mode, you can change it into 'r' to 'w' means you can write the data to a file

# Question 3
lyrics = [
'Here is a snippet of Elton John’s song “I’m Still Standing”\n',
 
"You could never know what it's like\n",
"Your blood like winter freezes just like ice\n",
"And there's a cold lonely light that shines from you\n",
"You'll wind up like the wreck you hide behind that mask you use\n",
 
"And did you think this fool could never win?\n",
"Well look at me, I'm coming back again\n",
"I got a taste of love in a simple way\n",
"And if you need to know while I'm still standing, you just fade away\n",
 
"Don't you know I'm still standing better than I ever did\n",
"Looking like a true survivor, feeling like a little kid\n",
"I'm still standing after all this time\n",
"Picking up the pieces of my life without you on my mind\n",
 
"I'm still standing (Yeah, yeah, yeah)\n",
"I'm still standing (Yeah, yeah, yeah)\n"
]
 
# Tasks:
# 1.   	Write the lyrics to a new file called song.txt
# 2.   	Check that a file has been created successfully.
# 3.   	The read lines from this file and print out ONLY those lines that have a word ‘still’ in them.

with open('song.txt', 'w') as song:
  song.writelines(lyrics)

with open('song.txt', 'r') as song:
  lyric = song.readlines()
  substring = 'still'
  for ly in lyric:
    if sub in ly:
      print(ly)

#  TASK 4 (API)

# Question 1
# In this session you used the Pokémon API to retrieve a single Pokémon.
# I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
# Use a list to store about 6 Pokémon IDs. 
# Then in a for loop call the API to retrieve the data for each Pokémon. 
# Save their names and moves into a file called 'pokemon.txt'

import requests

ids = [1,2,3,4,5,6]   ## create a list of ids

for id in ids:
  endpoint = f'https://pokeapi.co/api/v2/pokemon/{id}/'
  response = requests.get(endpoint)

  data = response.json()    ### get json file
  with open('pokeman.txt','w') as po:
    po.writelines(data['name'] + '\n')    ## write it to pokeman.txt
    po.writelines(str(data['moves']))


  with open('pokeman.txt','r') as po:
    print(po.read())