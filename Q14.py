# Q14  Write a program that reads multiple lines of input from the user until they
#enter an empty line, then prints all the lines
print("Enter multiple lines of input (press Enter on an empty line to finish):")
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\nYou entered:")
for line in lines:
    print(line)
