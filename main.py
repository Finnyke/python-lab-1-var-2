# LAB 1, VARIANT 2
# Maxim Pupykin, group 6312

import re
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

with open("text.txt", "r") as text:
    input_string = text.read()

letters = re.findall(r"([a-z]|[A-Z])", input_string)

results = open("results.txt", "w")

for letter in alphabet:
    results.write(letter + " - " + str(letters.count(letter) + letters.count(letter.upper())) + "\n")

results.close()
