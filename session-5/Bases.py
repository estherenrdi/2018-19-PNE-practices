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
