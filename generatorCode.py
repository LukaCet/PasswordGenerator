import random

letters = 'abcdefghijklmnopqrstuvwxyz'
letters_upper = letters.upper()
numbers = '1234567890'
special_characters = '!@#$%^&*()-_=+][;:.>,</?|\\'

everything = ""
if letters:
    everything += letters
if letters_upper:
    everything += letters_upper
if numbers:
    everything += numbers
if special_characters:
    everything += special_characters

minimum = int(input("Enter minimum password Length: "))
maximum = int(input("Enter maximum password Length: "))

amount = int(input("How many random passwords would you like: "))

for y in range(amount):
    password_length = random.randint(minimum, maximum + 1)
    password = "".join(random.sample(everything, password_length))
    print(password)
