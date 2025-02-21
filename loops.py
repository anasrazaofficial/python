import random

import math

# While Loop
# randomNum = math.floor((random.random() * 10) + 1)
# num = input("Guess a number between 1 and 10: ")
#
# while randomNum != int(num):
#     print("Wrong guess")
#     num = input("Guess again: ")
# print("Good guess!")

# For Loop
for i in "Python":
    print(i)

print("--------------")
for i in [1, 2, 3, 4]:
    print(i)

print("--------------")
for i in range(10):
    print(i)

print("--------------")
for i in range(5, 10):
    print(i)

print("--------------")
for i in range(0, 10, 2):
    print(i)

print("--------------")

# Print "F" shape
numbers = [5, 1, 5, 1, 1]
for i in numbers:
    print("*" * i)
