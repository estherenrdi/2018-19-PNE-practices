# Example of reading a file located in our local system

NAME = "mynotes.txt"

# OPEN THE FILE

myfile = open(NAME, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))
