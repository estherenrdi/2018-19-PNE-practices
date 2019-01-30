with open('CPLX2.txt', 'r') as f:
    count_A = 0
    count_T = 0
    count_C = 0
    count_G = 0
    valid_letters = ['A', 'T', 'C', 'G']
    for line in f:
        if '>' in line:
            line = line.replace(line, '')
        else:
            for letter in line:
                if letter == 'A':
                    count_A += 1
                elif letter == 'T':
                    count_T += 1
                elif letter == 'C':
                    count_C += 1
                elif letter == 'G':
                    count_G += 1
    print("A: ", count_A, "\nC: ", count_C ,"\nT: ", count_T, "\nG: ", count_G)












