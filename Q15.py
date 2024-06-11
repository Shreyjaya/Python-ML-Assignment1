# Q15 Write a program that reads data from a CSV file and prints it to the
#console.
import csv

samplefile=open("C:/Users/Shreyjaya/OneDrive/Desktop/1st Assignment/sample.csv",'r')
a=csv.reader(samplefile)
for row in a:
        print(', '.join(row))