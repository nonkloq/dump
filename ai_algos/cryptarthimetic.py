from itertools import permutations

def toInt(x,soln):
    n = 0
    p = 0
    for i in range(len(x)-1,-1,-1):
        n += soln[x[i]]*(10**p)
        p+=1
    return n

def isValid(a,b,c,soln):
    return toInt(a, soln) + toInt(b, soln) == toInt(c, soln)

def solve(a,b,c):
    words = list(set(a+b+c))
    solutions = []
    if len(words) > 10: return None
    for perm in permutations(range(10),len(words)):
        soln = {words[i]:perm[i] for i in range(len(words))}
        if isValid(a,b,c,{words[i]:perm[i] for i in range(len(words))}):
            solutions.append(soln)
    
    return solutions

a = "WHAT"
b = "THE"
c = "FUCK"
solutions = solve(a, b, c)
if solutions == None:   print("10+ letters can't be solved.")
if solutions == []: print("No Solution Exists")
else:
    for soln in solutions:
        print(soln)
        print(toInt(a, soln),'+',toInt(b, soln),'=',toInt(c, soln),'\n')