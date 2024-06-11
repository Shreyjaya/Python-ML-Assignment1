# Q25 Write a program that copies the contents of one text file to another
sourcefile='Samplefile.txt'
destination='Samplefile2.txt'
with open(sourcefile, 'r') as src:
        contents = src.read()
with open(destination, 'w') as dest:
        dest.write(contents)