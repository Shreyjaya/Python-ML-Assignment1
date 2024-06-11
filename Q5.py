# Q5 Write a program that takes a string input from the user and writes it to a
#text file.

a=input("enter the string ")
Samplefile=open('C:/Users/Shreyjaya/OneDrive/Desktop/1st Assignment/Samplefile.txt','w')
print(a,sep=' ',file=Samplefile)