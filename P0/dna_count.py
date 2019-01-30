user = str(input("Please introduce the sequence : ").upper())

print(len(user))

count_A = 0
count_T = 0
count_C = 0
count_G = 0
valid_letters = ['A', 'T', 'C', 'G']
for letter in user:
    if letter not in valid_letters:
        letter = letter.replace(letter, '')
    elif letter == 'A':
        count_A += 1
    elif letter == 'T':
        count_T += 1
    elif letter == 'C':
        count_C += 1
    elif letter == 'G':
        count_G += 1

print('A: ', count_A)
print('T: ', count_T)
print('C: ', count_C)
print('G: ', count_G)
