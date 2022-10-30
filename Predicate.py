from Function import Function


class Predicate:
    __slots__ = "var_const", "functions", "neg_flag", "name"

    def __init__(self, string):
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
                self.functions.append(Function(ind_string))
            else:
                self.var_const.append(ind_string)

    def __hash__(self):
        hash1 = 0
        for func in self.functions:
            hash1 += hash(func)
        for i in range(len(self.var_const)):
            hash1 += hash(self.var_const[i] + str(i))
        return hash(self.name) + hash1

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __str__(self):
        var = ""
        for v in self.var_const:
            var += v + ","
        for func in self.functions:
            var += str(func) + ","
        if var != "":
            var = "(" + var[:-1] + ")"
        var = self.name + var
        if self.neg_flag:
            var = "!" + var
        return var
