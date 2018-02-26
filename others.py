"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#use list comprehension for task4.

possible_phone_list = [x[0] for x in calls]
impossible_phone_list = sum([[x[0], x[1]] for x in texts], []) + [x[1] for x in calls]
telemarketers = sorted(set(possible_phone_list) - set(impossible_phone_list))

print("These numbers could be telemarketers: ")
for x in telemarketers:
    print('\n' + x)

shark_letters = [letter for letter in 'shark']
print(shark_letters)

#List Comprehensions
shark_letters =[]
for letter in 'shark':
	shark_letters.append(letter)
print(shark_letters)

#Using Conditionals with List Comprehensions
fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
fish_list = [fish for fish in fish_tuple if fish !='octopus']
print(fish_list)

number_list =[x ** 2 for x in range(10) if x%2 ==0]
print(number_list)

number_list =[x for x in range(10)]
print(number_list)

number_list =[x for x in range(10) if x%2 ==0]
print(number_list)

number_list =[x for x in range(100) if x%3 ==0 if x%5 ==0]
print(number_list)

#Nested Loops in a List Comprehension

my_list = []
for x in [20,40,60]:
	for y in [2,4,6]:
		my_list.append(x *y)
print(my_list)

my_list =[x *y for x in [20,40,60] for y in [2,4,6]]
print(my_list)