def subsetsum(A,d):
    solutions = []
    
    def backtrack(bag,A,d):
        if d == 0: 
            solutions.append(list(bag))
            return 
        if not A or d<0: return
        
        backtrack(bag+[A[-1]],A[:-1],d-A[-1])
        backtrack(bag,A[:-1],d)

    backtrack([],A,d)
    return solutions

A = [2,1,8,6,5]
d = 9
print(subsetsum(A,d))