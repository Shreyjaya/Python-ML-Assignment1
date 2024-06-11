# Q20 Write a python program that takes a list of numbers and returns their sum.

list1= eval(input("Enter the Numbers: "))
sum=0
for i in range(0,len(list1)):
     sum=sum+list1[i]
print("the sum of list is",sum)
    