# Task 3 (Password generator)

import random

print("Hello! This is your password generator.")
password_length = int(input("Enter the length of password you need: "))
password_count = int(input("Enter the number of passwords you need: "))

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST0123456789@#*&_"

for i in range(0, password_count):
    password= ""
    for j in range(0, password_length):
        password_character = random.choice(char)
        password = password + password_character

    print("Your required password is: ", password)

print("Thank you for using me!")