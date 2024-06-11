# Q19 Write a python program that removes all punctuation from a given string.
import string


str = input("enter the string")
no_punct = "".join(char for char in str if char not in string.punctuation)

print(no_punct)
