from Predicate import Predicate
class Clauses:
    __slots__ = "predicate","constants_list","variables_list","functions_list","predicates_list"

    def __init__(self,constants, variables, functions, predicates):
        self.constants_list = constants
        self.variables_list = variables
        self.functions_list = functions
        self.predicates_list = predicates
        self.predicate=[]

    def extractPredicate(self,string):
        data_list = string.strip().split(" ")
        for d in data_list:
            if d != "":
                self.predicate.append(Predicate(d,self.constants_list,self.variables_list,self.functions_list,self.predicates_list))

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

    def getNumVar(self):
        var=0
        for pred in self.predicate:
            var+=pred.getNumVar()

    def getNumConst(self):
        const=0
        for pred in self.predicate:
            const+=pred.getNumConst
        return const


    def hasConstant(self):
        return self.predicate[0].hasConstant()

    def hasVariable(self):
        return self.predicate[0].hasVariable()

    def makeConst(self,const):
        for pred in self.predicate:
            pred.makeConst(const)

    def changeVar(self,map1):
        for pred in self.predicate:
            pred.changeVar(map1)



