# Q21 Write a python program that counts the occurrences of a specific element
#in a list.

lst = input("enter the elements: ")


target_element=input("enter the target element: ")

count = lst.count(target_element)

print("The element", target_element, "occurs" ,count," times in the list.")
