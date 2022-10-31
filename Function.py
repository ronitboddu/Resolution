class Function:
    __slots__ = "variables", "name", "neg_flag", "constants_list", "predicates_list",\
                "functions_list","variables_list"

    def __init__(self, string,constants, variables, functions, predicates):
        self.constants_list = constants
        self.variables_list = variables
        self.functions_list = functions
        self.predicates_list = predicates
        self.variables = []
        self.neg_flag = False
        if string[0] == "!":
            self.neg_flag = True
            string = string[1:]
        index = string.find("(")
        if index != -1:
            self.name = string[:index]
            #print(string)
            inner_string = string[index + 1:-1]
            #print(inner_string)
            self.variables = inner_string.strip().split(",")
            #print(self.variables)
        else:
            self.name = None

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        hash1 = 0
        for elem in self.variables:
            hash1 += hash(elem)
        return hash(self.name) + hash1

    def __str__(self):
        var = ""
        for v in self.variables:
            var += v+","
        return self.name + "(" + var[:-1] + ")"

    def getNumVar(self):
        return len(self.variables)

    def makeConst(self,const):
        for i in range(len(self.variables)):
            if self.variables[i] in self.variables_list:
                self.variables[i] = const

    def changeVar(self,key,val):
        if key in self.variables:
            index = self.variables.index(key)
            self.variables[index] = val


    def getNumConst(self):
        const=0
        for v in self.variables:
            if v in self.constants_list:
                const+=1
        return const

    def hasVariable(self):
        for v in self.variables:
            if v in self.variables_list:
                return True
        return False

    def allConst(self):
        for v in self.variables:
            if v not in self.constants_list:
                return False
        return True

    def hasConstant(self):
        for v in self.variables:
            if v not in self.constants_list:
                #print(v)
                return False
        return True
