# student_height = input("Input the list of students height ").split()
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])
# print(student_height)
 
# total_height = 0
# for height in student_height:
#     total_height += height
# print(total_height)

# number_of_students = 0
# for student in student_height:
#     number_of_students += 1
# print(number_of_students)    
#---------------------------------------------
# student_scores = input("enter the list of scores for who got highest").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#      highest_score = score
# print(highest_score)
#---------------------------------Range function

# total = 0
# for number in range(1, 10):
#     total += number
# print(total)
#-------------------sum of all even numbers

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# to_tal = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#       to_tal += number
# print(to_tal)
#-----------------------FIZZ_BUZZ
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)
#---------------password generator
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print("char", char)

# convert list to string
pwd = ''.join(password_list)
print(f"Your random password to use is: {pwd}")








