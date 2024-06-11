# Q18 Write a python program that checks if two strings are anagrams of each
#other.
string1=input("Enter first string: ")
string2=input("Enter second string: ")
if sorted(string1)==sorted(string2):
    print("It is An Anagram")
else:
    print("It is not an Anagram")
