# Challenge 035
'''
name = input("Type your name: ")
for i in range(0, 3):
    print(name)
'''

# Challenge 036
'''
name = input("Type your name: ")
number = int(input("Enter a number: "))
for i in range(0, number):
    print(name)
'''

# Challenge 037
'''
name = input("Enter your name: ")
for i in name:
    print(i)
'''

# Challenge 038
'''
num = int(input("Enter a number: "))
name = input("Enter your name: ")
for x in range(0, num):
    for i in name:
        print(i)
'''

# Challenge 039
'''
num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
    answer = num * 1
    print(i, "x", num, "=", answer)
'''
# Challenge 040
'''
num = int(input("Enter a number below 50: "))
for i in range(50,num-1, -1):
    print(i)
'''

# Challenge 041
'''
name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0,3):
        print("To high")
'''

# Challenge 042
'''
total = 0
for i in range(0,5):
    num = int(input("Enter a number: "))
    ans = input("Do you want this number included? (y/n) ")
    if ans == "y":
        total = total + num
    print(total)
'''

# Challenge 043
'''
direction = input("Do you want to count up or down (u/d) ")
if direction == "u":
    num = int(input("What is the top number: "))
    for i in range(1, num + 1):
        print(i)
elif direction =="d":
    num =int(input("Enter a number below 20: "))
    for i in range(20, num - 1, -1):
        print(i)
else:
    print("I don't understand.")
'''

# Challenge 044
'''
num = int(input("How many friends do yo want to invite to the party? "))
if num < 10:
    for i in range(0, num):
        name = input("Enter a name: ")
        print(name, "has benn invited")
else:
    print("Too many people")
'''

# Challenge 045
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total = total + num
    print("The total is ....", total)










# Challenge 046













# Challenge 047










# Challenge 048











# Challenge 049











# Challenge 050












# Challenge 051


# Challenge 080
'''fname = input("Enter your first name: ")
print("That has", len(fname), "characters in it\n")
sname = input("Enter your surname: ")
print("That has", len(sname), "characters in it\n")
name = fname + " " + sname
print("Your full name is", name)
print("That has", len(name), "characters in it")'''

# Challenge 081
'''
import random
subject = input("Enter your favorite school subject: ")
for letter in subject:
    print(letter,end="_")
'''

# Challenge 082
'''
poem = "Oh, I wish I'd loocked after me teeth,"
print(poem)
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))
print(poem[start:end]) '''


# Challenge 083
# msg = input("Enter a massage in uppercase: ")
# tryagain = False
# while tryagain == False:
#     if msg.isupper():
#         print("Thank you")
#         tryagain = True
#     else:
#         print("Try again")
#         msg = input("Enter a massage in uppercase: ")


# Challenge 084
# postcode = input("Enter your postcode: ")
# start = postcode[0:5]
# print(start.upper())

# Challenge 085
# name = input("Enter your name: ")
# count = 0
# name = name.lower()
# for x in name:
#     if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#         count = count + 1
#         print("vowels =", count)

# Challenge 086
# pswd1 = input("Enter your password: ")
# pswd2 = input("Enter it again: ")
# if pswd1 == pswd2:
#     print("Thank you")
# elif pswd1.lower() == pswd2.lower():
#     print("They must be the same case")
# else:
#     print("incorrect")

# Challenge 087
# word = input("Enter a word: ")
# length = len(word)
# num = 1
# for x in word:
#     position = length - num
#     letter = word[position]
#     print(letter)
#     num = num + 1


# Exemple array
# Challenge 088

# from array import array

# nums = array('i', [])

# for i in range (0,5):
#     num = int(input("Enter a number: "))
#     nums.append(num)

# nums = sorted(nums)
# nums.reverse()
# print(nums)

# Challenge 089
"""
from array import *
import random

nums = array('i',[])

for i in range (0,5):
    num = random.randint(1,100)
    nums.append(num)
for i in nums:
    print(i)
"""

# Challenge 090
"""
from array import *

nums = array('i',[])
while len(nums) < 5:
    num = int(input("Enter a number between 10 and 20: "))
    if num >= 10 and num <= 20:
        nums.append(num)
    else:
        print("Outside the range")

for i in nums:
    print(i)
"""

# Challenge 091
"""
from array import *

nums = array('i',[5,7,9,2,9])

for i in nums:
    print(i)

num = int(input("Enter a number: "))

if nums.count(num) == 1:
    print(num, "is in the list once")
else:
    print(num, "is in the list", nums.count(num), "times")
"""

# Challenge 092
"""
from array import *
import random

num1 = array('i',[])
num2 = array('i',[])

for i in range(0,3):
    num = int(input("Enter a number: "))
    num1.append(num)

for i in range(0,5):
    num = random.randint(1,100)
    num2.append(num)

num1.extend(num2)
num1 = sorted(num1)

for i in num1:
    print(i)
"""

# Challenge 093
"""
from array import *

nums = array('i',[])

for i in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)

num = int(input("Select a number from the array: "))
if num in nums:
    nums.remove(num)
    num2 = array('i',[])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That is not a value in the array")
"""

# Challenge 094
"""
from array import *
from functools import total_ordering

nums = array('i',[4,6,8,2,5])

for i in nums:
    print(i)

num = int(input("Select one of the  number: "))

tryagain = True
while tryagain == True:
    if num in nums:
        print("This is in position", nums.index(num))
        tryagain = False
    else:
        print("Not in array")
        num = int(input("Select one of rhe number: "))
"""

# Challenge 095
# from array import *
# import math

# nums = array('f',[34.75, 27.23,99.58,45.26,28.65])
# tryagain = True
# while tryagain == True:
#     num = int(input("Enter a number between 2 and 5: "))
#     if num < 2 or num > 5:
#         print("incorrect value, try again.")
#     else:
#         tryagain = False
# for i in range(0,5):
#     ans = nums[i]/num
#     print(round(ans,2))

# Challenge 096
# list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

# Challenge 097
'''
list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("Select a row: "))
col = int(input("Select a column: "))
print(list[row][col])
'''
# Challenge 098
'''
list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("Select a row: "))
print(list[row])
newvalue = int(input("Enter a new value: "))
list[row].append(newvalue)
print(list[row])
'''
# Challenge 099
'''
list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("Select a row: "))
col = int(input("Select a column: "))
print(list[row][col])
change = input("Do you want to change the value? (y/n) ")
if change == "y":
    newvalue = int(input("Enter a new value: "))
    list[row][col] = newvalue
print(list[row])
'''

# Challenge 100

# from os import read

# sales = {"Jhon":{"N": 3056, "S":8463, "E":8441, "W":2694},
# "Tom":{"N": 4832, "S":6786, "E":4737, "W":3612},
# "Anne":{"N": 5239, "S":4802, "E":5820, "W":1859},
# "Fiona":{"N": 3904, "S":3645, "E":8821, "W":2451}}

# Challenge 101
'''
sales = {"Jhon":{"N": 3056, "S":8463, "E":8441, "W":2694},
"Tom":{"N": 4832, "S":6786, "E":4737, "W":3612},
"Anne":{"N": 5239, "S":4802, "E":5820, "W":1859},
"Fiona":{"N": 3904, "S":3645, "E":8821, "W":2451}}

person = input("Enter sales person's name: ")
region = input("Select region: ")
print(sales[person] [region])

newdata = int(input("Enter new data: "))
sales[person][region] = newdata
print(sales[person])

'''
# Challenge 102
# list = {}
# for i in range (0,4):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     shoe = int(input("Enter shoe size: "))
#     list [name] = {"Age": age, "shoe size": shoe}

# ask = input("Enter a name: ")
# print(list[ask])

# Challenge 103
'''
list = {}
for i in range (0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list [name] = {"Age": age, "shoe size": shoe}

for name in list:
    print((name),list[name] ["Age"])
'''
# Challenge 104
# list = {}
# for i in range (0,4):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     shoe = int(input("Enter shoe size: "))
#     list [name] = {"Age": age, "shoe size": shoe}

# getrid = input("Who do you want to remove from the list? ")
# del list[getrid]

# for name in list:
#     print((name),list[name] ["Age"])


# Challenge 105
# Reading and writing
'''
file = open("Numbers.txt","w")
file.write("4, ")
file.write("6, ")
file.write("10, ")
file.write("8, ")
file.write("5, ")
file.close()

'''

# Challenge 106
# file = open("Names.txt","w")
# file.write("Bob\n")
# file.write("Tom\n")
# file.write("Gemma\n")
# file.write("Sarah\n")
# file.write("Timothy\n")
# file.close()


# Challenge 107
'''
file = open("Names.txt","r")
print(file.read())
file.close()
'''

# Challenge 108
'''
file = open("Names.txt","a")
newname = input("Enter a new name: ")
file.write(newname + "\n")
file.close

file = open("Names.txt","r")
print(file.read())
file.close
'''

# Challenge 109
'''
print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = int(input("Make a selection 1, 2 or 3: "))
if selection == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt","w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("subject.txt","r")
    print(file.read())
elif selection == 3:
    file = open("subject.txt","a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("subject.txt","r")
    print(file.read())
else:
    print("Invalid option.")
'''


# Challenge 110
'''
file = open("Names.txt","r")
print(file.read())
file.close()

file = open("Names.txt","r")
selectedname = input("Enter a name from the list: ")
selectedname = selectedname + "\n"
for row in file:
    if row != selectedname:
        file = open("Names2.txt","a")
        newrecord = row
        file.write(newrecord)
        file.close()
file.close
'''

# Challenge 111
'''
import csv

file = open("Books.csv","w")
newrecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newrecord))
newrecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Great Gatsby, F. Scort Fitzgerald, 1922\n"
file.write(str(newrecord))
newrecord = "The man who Mistook His Wife for a Hat, oliver Saks, 1985\n"
file.write(str(newrecord))
newrecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newrecord))
file.close()

'''

# Challenge 112

















# Challenge 113














# Challenge 114
















# Challenge 115


