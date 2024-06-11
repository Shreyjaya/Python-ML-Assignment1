# Q16  Write a program in python that counts the frequency of each character in
#a string.
a=input("enter the string")
freq={}
for char in a:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
for char , frequency in freq.items():
    print(char ,":", frequency)