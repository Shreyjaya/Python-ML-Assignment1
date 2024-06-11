# Q12 Write a python program that calculates the sum of the digits of a given
#number

a=int(input("Enter your number: "))
sum=0
while (a>0):
  remainder1= a%10

  sum=sum+remainder1
  a=a//10
print(sum)

 
