print("Hello World")
print("This is a test file.")
sum int((2, 3))
print("Sum of 2 and 3 is:", sum(2, 3))
print("Sum of 2 and 3 is:",  ([2, 3]))

import re
import statistics

numbers = [2, 3, 4]
avg = statistics.mean(numbers)
print("Average is:", avg)
a=3
b=4
print("Product is:", a*b)
--------
name='John'
age=30 
print(f'My name is {name} and I am {age} years old.')
print('My name is {} and I am {} years old.'.format(name, age))
print('My name is %s and I am %d years old.' % (name, age))

x=10
y=20
print(f'Sum of x and y is {x+y}')

regular_string = 'C:\new_folder\test.txt'
print('regular_string:', regular_string)

raw_string = r'C:\new_folder\test.txt'
print('raw_string:', raw_string)

import re

pattern = r'\d\d\d\d\d\d\d\d\d\d'
text = 'My phone number is 1234567890.'
match = re.search(pattern, text)

if match:
    print('Phone number found:', match.group())
else:
    print('Match not found.')

noncharacter_pattern = r'\W'
s2 = 'The Bodyguard is the best album of \'Whitney Houston\'.'
result = re.findall(noncharacter_pattern, s2)
print('Occurrences of "st":', result)
"helloMike".find("Mike")

my_string="Hello" 
char = my_string[0]
print(char)

'maria'+'rodrigez'

L = ['The bodyguard', 7.0, 'pop']
L.extend(['pop', 1980])
L

A = ['disco', 10, 'Michael Jackson']
A.extend(['pop', 1980]) 
A

print('Before change:', A)
A[0]= 'hard rock'
print('After change:', A)

a = {'rap','house','electronic music', 'rap'}
set1 = set(a)
set1

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("They are equal:", sum(A) == sum(B))

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
album_set1.issubset(album_set3)
album_set1.issubset(album_set2)

album_set1.add("NSYNC")
album_set1 

my_tuple = ('disco', 10, 1.2)
my_tuple.append(5)

my_list = list(my_tuple)
my_list
my_list.append(5)
my_list

empty_set = set() #Creating an Empty Set 
fruits = {"apple", "banana", "orange"}
colors = ("orange", "red", "green")

age=19
if age < 18:
    age = 19
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
album_year = 1983
if (album_year != 1984):
album_year = 1983
if album_year != 1984:
    print("Album year is not 1984")
sport = 'Soccer'
player_name = 'Lionell Messi'
sport = 'Soccer'
achievements = 7
if achievements >= 10:
    print(f"{player_name} plays {sport} and has {achievements} achievements")
else:
    print(f'{player_name} doesn\'t have more than 10 achievements')
player_name = 'Serena Williams'
sport = 'Tennis'
achievements = 23
if sport == 'Tennis' or achievements == 20:
    print(f"{player_name} meets the criteria! They play {sport} or have {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")
friend1_likes_comedy = True
friend2_likes_action = False
friend3_likes_drama = False
if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
    print("choose_a_movie")

user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    while True:
        amount = int(input("Enter the amount to withdraw: "))
        if amount == 0: 
            print("Don't play with me bitch")
            break
        if amount % 10 == 0:
            print("You have chosen to withdraw:", amount)
            print("Amount dispensed: ", amount)
            break
        else:
            print("Please enter a multiple of 10.")
    print("Thank you for using the ATM.")

squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

def sum(a, b):
    pass

a = sum(5, 10)
print(a)

def print_numbers(limit):
    for i in range(1, limit+1):
        print(i*)

print_numbers(5)

def factorial(n):
    result = 1          # start from 1
    for i in range(1, n + 1):
        result *= i     # same as result = result * i
    return result

print(factorial(5))     # 120


def factorial(number):
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


print(factorial(int(input("please enter a number: "))))

def greet(name):
    for i in range(2, 4):
        print("Hello, " + name)

print(greet("Alice"))
greet("Bob")

def greet(name):
    message = ""
    for i in range(2, 4):
        message += "Hello, " + name + "\n"
    return message

print(greet("Alice"))

def haha(a):
    result = 'Wooohoooo'
    return result

haha(a)

my_list = [1, 2, 3]

def add_element(my_list, element):
    my_list.append(element)

add_element(my_list, {4,5,6})
print(my_list)

def sum(a, b):
result = a + b
return result

print(sum(2, 3))

for i in range(5):
    pass
    if i:
    pass
    ifelse i == 3:
    print(i)

def remove_data(data_list, item):
    if item in data_list:
        data_list.remove(item)
        return True
    else:
        print("Item not found in the list.")
        return False

data = [1, 2, 3, 4, 5]
x = int(input("Insert the data to be removed here: "))

if remove_data(data, x):
    print(f"{x} has been successfully removed. Updated data: {data}")

def add_element(my_list, elemrnt):
    

