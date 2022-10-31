from Function import Function


class Predicate:
    __slots__ = "var_const", "functions", "neg_flag", "name", "constants_list", "predicates_list", \
                "functions_list", "variables_list"

    def __init__(self, string, constants, variables, functions, predicates):
        self.constants_list = constants
        self.variables_list = variables
        self.functions_list = functions
        self.predicates_list = predicates
        self.functions = []
        self.var_const = []
        self.neg_flag = False
        self.name = ""
        if len(string) > 0:
            if string[0] == "!":
                self.neg_flag = True
                string = string[1:]
            index = string.find("(")
            if index != -1:
                self.name = string[:index]
                inner_string = string[index + 1:-1]
                self.extractInner(inner_string)
            else:
                self.name = string

    def extractInner(self, inner_string):
        ind = inner_string.strip().split(",")
        for ind_string in ind:
            if "(" in ind_string:
                self.functions.append(
                    Function(ind_string, self.constants_list, self.variables_list, self.functions_list,
                             self.predicates_list))
            else:
                self.var_const.append(ind_string)

    def __hash__(self):
        hash1 = 0
        # for func in self.functions:
        #     hash1 += hash(func)
        # for i in range(len(self.var_const)):
        #     if self.var_const[i] in self.constants_list:
        #         hash1 += hash(self.var_const[i] + str(i))
        return hash(self.name) + hash1

    def __eq__(self, other):
        #print(self,other)
        #print(self,self.hasConstant())
        #print(self.var_const)
        if (self.hasConstant() and not other.hasConstant()) or (not self.hasConstant() and other.hasConstant()):
            #print(hash(self),hash(other))
            return hash(self) == hash(other)
        else:
            hash1, hash2 = 0, 0
            for i in range(len(self.var_const)):
                if self.var_const[i] in self.constants_list:
                    hash1 += hash(self.var_const[i] + str(i))
            for j in range(len(other.var_const)):
                if other.var_const[j] in other.constants_list:
                    hash2 += hash(other.var_const[j] + str(j))
            return hash(self) + hash1 == hash(other) + hash2

    def __str__(self):
        var = ""
        for v in self.var_const:
            var += str(v) + ","
        for func in self.functions:
            var += str(func) + ","
        if var != "":
            var = "(" + var[:-1] + ")"
        var = self.name + var
        if self.neg_flag:
            var = "!" + var
        return var

    def getNumVar(self):
        var = 0
        for func in self.functions:
            var += func.getNumVar()
        for v in self.var_const:
            if v in self.variables_list:
                var += 1
        return var

    def getNumConst(self):
        const = 0
        for func in self.functions:
            const += func.getNumConst()
        for v in self.var_const:
            if v in self.constants_list:
                const += 1
        return const

    def changeVar(self, map1):
        for key in map1:
            if key in self.var_const:
                index = self.var_const.index(key)
                self.var_const[index] = map1[key]
            for func in self.functions:
                func.changeVar(key, map1[key])

    def makeConst(self, const):
        for func in self.functions:
            func.makeConst(const)
        for i in range(len(self.var_const)):
            if self.var_const[i] in self.variables_list:
                self.var_const[i] = const

    def hasConstant(self):
        #print(self.var_const)
        for c in self.var_const:
            if c not in self.constants_list:
                #print(c in self.constants_list)
                return False
        for func in self.functions:
            #print("in func")
            return func.hasConstant()
        return True

    def hasVariable(self):
        for v in self.var_const:
            if v in self.variables_list:
                return True
        for func in self.functions:
            return func.hasVariable()
        return False

    def getConst(self):
        const_list = []
        for c in self.var_const:
            if c in self.constants_list:
                const_list.append(c)
        return const_list

    def getVarConst(self):
        return self.var_const + self.functions

    def allConst(self):
        for v in self.var_const:
            if v not in self.constants_list:
                return False
        for func in self.functions:
            return func.allConst()
        return True
