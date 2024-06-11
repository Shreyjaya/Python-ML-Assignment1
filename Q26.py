#26. Write a program in python that checks if a string starts with a given prefix
#or ends with a given suffix

a=input("enter the string: ")
b=input("enter the prefix: ")
c=input("enter the suffix: ")
if a.startswith(b):
    print("The string starts with the prefix ",b)
else:
    print("The string does not start with the prefix ",b)
if a.endswith(c):
    print("The string ends with the suffix", c)
else:
    print("The string does not end with the suffix",c)

