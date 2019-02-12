# Example of reading a file located in our local system

NAME = "mynotes.txt"

# OPEN THE FILE

myfile = open(NAME, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()

f = open(NAME, 'a')

f.write("THIS IS A TEXT EXAMPLE AND MIRIAM IS IN TINDER ")

f.close()

print("The end")