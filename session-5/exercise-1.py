def count_letter(sequence, lett):
    count_let = sequence.count(lett)
    return count_let


def count_bases(seq):
    dict_s = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    count_a = count_letter(seq, 'A')
    dict_s['A'] = count_a

    count_t = count_letter(seq, 'T')
    dict_s['T'] = count_t

    count_c = count_letter(seq, 'C')
    dict_s['C'] = count_c

    count_g = count_letter(seq, 'G')
    dict_s['G'] = count_g
    return dict_s


def percentage(seq):
    tl = len(seq)
    list_per = list()
    if tl > 0:
        n_a = round(100.0 * count_bases(seq)['A'] / tl, 1)
        list_per.append(n_a)
        n_t = round(100.0 * count_bases(seq)['T'] / tl, 1)
        list_per.append(n_t)
        n_c = round(100.0 * count_bases(seq)['C'] / tl, 1)
        list_per.append(n_c)
        n_g = round(100.0 * count_bases(seq)['G'] / tl, 1)
        list_per.append(n_g)

    else:
        perc = 0

    return list_per


def main_programe():
    seq = str(input("Enter the sequence : ").upper())

    print("This sequence is {} bases in lenght".format(len(seq)))

    print("Base A\n\tCounter: " ,count_bases(seq)['A'],"\n\tPercentage :",percentage(seq)[0])
    print("Base T\n\tCounter: " ,count_bases(seq)['T'],"\n\tPercentage :",percentage(seq)[1])
    print("Base C\n\tCounter: " ,count_bases(seq)['C'],"\n\tPercentage :",percentage(seq)[2])
    print("Base G\n\tCounter: " ,count_bases(seq)['G'],"\n\tPercentage :",percentage(seq)[3])


print(main_programe())
