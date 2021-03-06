def count_a(seq):
    """Counting the number of As in a sequence"""
    total_a = 0

    for element in seq:

        if element == 'A':
            total_a += 1

    return total_a


# Main program
s = input("Please, enter a sequence")
na = count_a(s)
print("The number of As is : {}".format(na))

#Calculate the length
tl = len(s)

#calculate the percentaje of As
if tl > 0:
    perc = round(100.0 * na / tl, 1)
else:
    perc = 0

print("The total length is : {}".format(tl))
print("The percentaje of As is {}%".format(perc))