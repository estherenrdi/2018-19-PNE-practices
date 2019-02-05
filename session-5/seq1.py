class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("new empty seq!")
        self.strbases = strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the seq
        All the objects of class Gene will
        inheritage the methods from seq class"""

s1 = Gene("AATTGATGATGATGATGATCCCCC")
s2 = Seq("AATTCC")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("sequence 1: {}".format(str1))
print("Lengt: {}".format(l1))
print("sequence 2: {}".format(str2))
print("Lengt: {}".format(l2))
print("The end happy and safe ")
