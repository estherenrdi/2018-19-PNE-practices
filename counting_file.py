def count_letters(filename):
    with open(filename, 'r') as f:

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
