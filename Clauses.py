from Predicate import Predicate
class Clauses:
    __slots__ = "predicate"

    def __init__(self):
        self.predicate=[]

    def extractPredicate(self,string):
        data_list = string.strip().split(" ")
        for d in data_list:
            if d != "":
                self.predicate.append(Predicate(d))

    def __str__(self):
        string = ""
        for p in self.predicate:
            string += str(p) + " "
        return string

    def __hash__(self):
        hash1 = 0
        hash1 += (hash(elem) for elem in self.predicate)
        return hash1

    def __eq__(self, other):
        return hash(self) == hash(other)

    def addPredicates(self, lst):
        if lst:
            self.predicate += lst
