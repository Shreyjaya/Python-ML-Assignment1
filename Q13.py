# Q13 Write a program that asks the user for their birth year and calculates their
#age.
from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age


birth_year = int(input("Enter your birth year: "))


age = calculate_age(birth_year)

print("your age is",age)