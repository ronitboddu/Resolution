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
            self.name = string[:index + 1]
            inner_string = string[index + 1:-1]
            self.variables = inner_string.strip().split(",")
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

    def changeVar(self,const):
        for i in range(len(self.variables)):
            if self.variables[i] in self.variables_list:
                self.variables[i] = const

    def getNumConst(self):
        const=0
        for v in self.variables:
            if v in self.constants_list:
                const+=1
        return const

