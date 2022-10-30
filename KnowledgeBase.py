from Clauses import Clauses


class KnowledgeBase:
    __slots__ = "clauses","predicates","variables","constants","functions"

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
                    cl = Clauses()
                    cl.extractPredicate(line)
                    self.clauses.append(cl)

    def process(self, lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                ans, flag = unify(lst[i], lst[j])
                if flag:
                    if len(ans) == 0:
                        return False
                    temp = lst.copy()
                    temp.pop(j)
                    temp.pop(i)
                    temp += ans
                    if not self.process(temp):
                        return False
        return True


def unify(clause1, clause2):
    ans = []
    flag = False
    for i in range(len(clause1.predicate)):
        for j in range(len(clause2.predicate)):
            if clause1.predicate[i] == clause2.predicate[j] and \
                    clause1.predicate[i].neg_flag != clause2.predicate[j].neg_flag:
                pred_lst = clause1.predicate[:i] + clause1.predicate[i + 1:] \
                                         + clause2.predicate[:j] + clause2.predicate[j + 1:]
                if pred_lst:
                    new_clause = Clauses()
                    new_clause.addPredicates(pred_lst)
                    ans.append(new_clause)
                flag = True
    return ans, flag


if __name__ == '__main__':
    k = KnowledgeBase("D:\\RIT\\sem2\\AI\\Lab2\\testcases(1)\\testcases\\constants\\c09.cnf")
    #k = KnowledgeBase("test.txt")
    temp = k.process(k.clauses)
    print('yes' if temp else 'no')
