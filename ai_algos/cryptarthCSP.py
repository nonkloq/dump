from csp_solvers import BacktrackingSearch

def toInt(x,assignment):
    n = 0
    p = 0
    for i in range(len(x)-1,-1,-1):
        n += assignment[x[i]]*(10**p)
        p+=1
    return n

def inference(assignment,variables,addend,result):
    if len(set(assignment.values())) < len(assignment): return False
    if len(assignment) < len(variables): return True
    Sum = 0
    for word in addend:
        number= toInt(word, assignment)
        Sum += number
    return Sum == toInt(result,assignment)

def SolveCryptArithmetic(addend,result):
    # formating the inputs
    for i in range(len(addend)): addend[i] = addend[i].upper()
    result = result.upper()
    
    # making csp
    variables = set(''.join(addend+[result]))
    if len(variables)>10: return False # invalid

    D = list(range(10))
    csp = (variables,D)

    return BacktrackingSearch(csp,lambda assignment: inference(assignment,variables,addend,result))

addend = ["SO","MANY","MORE","MEN","SEEM","TO","SAY","THAT","THEY","MAY","SOON","TRY","TO","STAY","AT","home",
    "SO","AS","TO","SEE","OR","HEAR","THE","SAME","ONE","MAN","TRY","TO","MEET","THE","TEAM","ON","THE","MOON","AS","HE",
    "HAS","AT","THE","OTHER","TEN"]

result = "tests"
print(SolveCryptArithmetic(addend,result))
