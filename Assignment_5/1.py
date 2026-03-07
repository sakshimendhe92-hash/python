# Practical No: 6
# Lab Assignment – 1

# Question:
# Develop an application which asks the user to enter a string
# and prints its statistics as:
# 1) Number of Vowels
# 2) Number of Consonants
# 3) Number of Spaces
# 4) Number of Lowercase Letters

string = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for ch in string:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    
    if ch == " ":
        spaces += 1
        
    if ch.islower():
        lowercase += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)