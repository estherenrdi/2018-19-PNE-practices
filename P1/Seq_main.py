#  Here is my main program requested for the practice 1
from Seq import Seq

s1 = Seq(input("Please, introduce a valid sequence1 : "))
s2 = Seq(input("\nPlease, introduce a valid sequence2 : "))
s3 = s1.complement()
s3 = Seq(s3)
s4 = s3.reverse()
s4 = Seq(s4)
print("Sequence 1: {}".format(s1.strbases), "\n\tLenght : {}".format(s1.len()), "\n\tThe number of As, Ts, Cs and Gs: {}".format(s1.count_bases()))
print("\tThe percentage of As: {} \n\tThe percentage of Ts: {} \n\tTHe percentage of Cs: {} \n\tThe percentage of Gs: {} ".format(s1.perc()[0], s1.perc()[1], s1.perc()[2], s1.perc()[3]))

print("Sequence 2: {}".format(s2.strbases), "\n\tLenght : {}".format(s2.len()), "\n\tThe number of As, Ts, Cs and Gs: {}".format(s2.count_bases()))
print("\tThe percentage of As: {} \n\tThe percentage of Ts: {} \n\tTHe percentage of Cs: {} \n\tThe percentage of Gs: {} ".format(s2.perc()[0], s2.perc()[1],s2.perc()[2], s2.perc()[3]))

print("Sequence 3: {}".format(s3.strbases), "\n\tLenght : {}".format(s3.len()), "\n\tThe number of As, Ts, Cs and Gs: {}".format(s3.count_bases()))
print("\tThe percentage of As: {} \n\tThe percentage of Ts: {} \n\tTHe percentage of Cs: {} \n\tThe percentage of Gs: {} ".format(s3.perc()[0], s3.perc()[1], s3.perc()[2], s3.perc()[3]))

print("Sequence 4: {}".format(s4.strbases), "\n\tLenght : {}".format(s4.len()), "\n\tThe number of As, Ts, Cs and Gs: {}".format(s4.count_bases()))
print("\tThe percentage of As: {} \n\tThe percentage of Ts: {} \n\tTHe percentage of Cs: {} \n\tThe percentage of Gs: {} ".format(s4.perc()[0], s4.perc()[1], s4.perc()[2], s4.perc()[3]))


