# open the file and read all the information
import json
import termcolor

f = open("person.json", 'r')

person = json.load(f)

print()

termcolor.cprint("Name: ",'green', end = '')
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ",'green', end = '')
print(person['age'])
print(person["phonenumber"])

for i, num in enumerate(person['phonenumber']):
    termcolor.cprint("Phone : {}".format(i), 'red', end='')
    termcolor.cprint('  Type:','green', end = '')
    print(num['type'])
    termcolor.cprint('  Number:', 'green', end='')
    print(num['number'])
