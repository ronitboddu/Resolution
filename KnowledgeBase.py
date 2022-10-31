from collections import defaultdict

from Clauses import Clauses


class KnowledgeBase:
    __slots__ = "clauses", "predicates", "variables", "constants", "functions"

    def __init__(self, filename):
        self.clauses = []
        self.predicates = []
        self.variables = []
        self.constants = []
        self.functions = []
        self.readFile(filename)

    def readFile(self, filename):
        with open(filename) as f:
            clause_flag = False
            for line in f:
                if 'Predicates' in line:
                    self.predicates = line.strip().split(" ")[1:]
                elif 'Variables' in line:
                    self.variables = line.strip().split(" ")[1:]
                elif 'Constants' in line:
                    self.constants = line.strip().split(" ")[1:]
                elif 'Functions' in line:
                    self.functions = line.strip().split(" ")[1:]
                if 'Clauses' in line:
                    clause_flag = True
                    continue
                if clause_flag:
                    cl = Clauses(self.constants, self.variables, self.functions, self.predicates)
                    cl.extractPredicate(line)
                    self.clauses.append(cl)

    def process(self, lst):
        for i in range(len(lst)):
            new_list = []
            for j in range(i + 1, len(lst)):
                temp = lst.copy()
                ans, flag = self.unify(temp[i], temp[j])
                new_list += ans
                if flag:
                    if len(ans) == 0:
                        return False
                    temp.pop(j)
                    temp.pop(i)
                    temp += ans
                    if not self.process(temp):
                        return False
            if not self.process(new_list):
                return False
        return True

    def unify(self, clause1, clause2):
        ans = []
        flag = False

        for i in range(len(clause1.predicate)):
            for j in range(len(clause2.predicate)):
                if clause1.predicate[i] == clause2.predicate[j] and \
                        clause1.predicate[i].neg_flag != clause2.predicate[j].neg_flag:
                    # print("here")
                    self.checkConditions(clause1, clause2, clause1.predicate[i], clause2.predicate[j])
                    pred_lst = clause1.predicate[:i] + clause1.predicate[i + 1:] \
                               + clause2.predicate[:j] + clause2.predicate[j + 1:]
                    if pred_lst:
                        new_clause = Clauses(self.constants, self.variables, self.functions, self.predicates)
                        new_clause.addPredicates(pred_lst)
                        ans.append(new_clause)
                        print(new_clause)
                    flag = True
        return ans, flag

    def checkConditions(self, clause1, clause2, pred1, pred2):
        # if self.variables and not self.constants:
        # print(pred1,pred2)
        if pred1.hasVariable() and pred2.hasVariable():
            clause1.makeConst("newVar")
            clause2.makeConst("newVar")
        elif self.variables and self.constants:
            if pred1.hasConstant() and pred2.hasVariable():
                map1 = self.mapVarConst(pred1.getVarConst(), pred2.getVarConst())
                clause2.changeVar(map1)
            elif pred2.hasConstant() and pred1.hasVariable():
                map1 = self.mapVarConst(pred2.getVarConst(), pred1.getVarConst())
                clause1.changeVar(map1)

    def mapVarConst(self, varConst1, varConst2):
        map1 = defaultdict(str)
        for i in range(len(varConst2)):
            if varConst2[i] in self.variables:
                map1[varConst2[i]] = varConst1[i]
        return map1


if __name__ == '__main__':
    k = KnowledgeBase("D:\\RIT\\sem2\\AI\\Lab2\\testcases(1)\\testcases\\functions\\f2.cnf")
    #k = KnowledgeBase("test.txt")
    temp = k.process(k.clauses)
    print('yes' if temp else 'no')
