# Here is my main programe for the practice1

from Seq import Seq

s1 = Seq(input("Please, introduce the sequence 1: "))
s2 = Seq(input("Please, introduce the sequence 2: "))
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())


print("The sequence number 1 is : {}".format(s1.strbases), "\nIt's length is : {}".format(s1.len()), "\nThe number of bases is : {}".format(s1.count_bases()), "\nThe p : {}".format(s1.perc()[0]))
print(s2.strbases)
print(s3.strbases)
print(s4.strbases)






