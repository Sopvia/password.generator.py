import random
import string
import secrets

letters= string.ascii_letters
digits = string.digits
symbols = string.punctuation

letter, nums, syms = True, True, True

characters = ''
if letter:
    characters += letters
if nums:
    characters += digits
if syms:
    characters += symbols

length = 12
amount = 10

for x in range(amount):
    password = ''.join(random.choice(characters) for i in range(length))
    print(password)