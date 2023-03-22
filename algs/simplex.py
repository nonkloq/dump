import numpy as np
INF = float('inf')

def printTableau(tableau):
    for row in tableau:
        print(row)
    print()


def addSlack(c,A):
    n = len(A)
    i = 0
    while i<n:
        c.append(0)
        A[i] += [1 if i == j else 0 for j in range(n)]
        i+=1

def makeTableau(c, A, b):
    tableau = [row + [x] for row, x in zip(A, b)]
    tableau.append(c + [0])
    return tableau

def canImprove(tableau):
    return any(x > 0 for x in tableau[-1][:-1])

def getPivot(tableau):
    lastrow = tableau[-1]
    column = next(i for i, x in enumerate(lastrow[:-1]) if x > 0)
    
    ratio = []
    for eq in tableau[:-1]:
        el = eq[column]
        ratio.append(INF if el <= 0 else eq[-1] / el)

    row = ratio.index(min(ratio))
    return row, column

def nextTableau(tableau, i,j):
    
    tableau[i] = np.array(tableau[i]) / tableau[i][j]
    
    for k, row in enumerate(tableau):
        if k != i:
            tableau[k] = np.array(tableau[k]) - (np.array(tableau[i]) * tableau[k][j])
   

def isBasic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns:
        solution = 0
        if isBasic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
        
    return solutions

def simplex(c, A, b):
    addSlack(c,A)
    tableau = makeTableau(c, A, b)
    j = 1
    while canImprove(tableau):
        print("Iteration",j)
        printTableau(tableau)

        pivot = getPivot(tableau)
        nextTableau(tableau, *pivot)
        j+=1
    return tableau, solution(tableau), -1*tableau[-1][-1]

c = [3,5]
A = [[1,1],[1,3]]
b = [4,6]

tableau,a,n = simplex(c,A,b)
print("Solution: ")
printTableau(tableau)
print("Soln:",a)
print("Maximum Value:",n)