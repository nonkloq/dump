from queue import PriorityQueue

def min_except(costs,assignment):
    out = float('inf')
    
    for job in range(len(costs)):
        if job in assignment: continue
        if costs[job] < out: out = costs[job]
    
    return out

def lowerbound(assignment,C):
    m = len(assignment)
    lb = 0
    for i in range(len(C)):
        if i < m: lb += C[i][assignment[i]]
        else: lb += min_except(C[i],assignment)
    return lb


def assign(assignment,job):
    if job in assignment: return None
    return assignment+[job]

def findAssignments(C):
    """Best First Branch and Bound"""
    n = len(C)
    Q = PriorityQueue()
    start = (lowerbound([],C),[])
    Q.put(start)

    optimal = (float('inf'),[])

    while Q.qsize()>0:
        lb, assignment = Q.get()
        if lb > optimal[0]: continue

        if len(assignment) == n: 
            if lb < optimal[0]: optimal = (lb,assignment)
            continue

        for job in range(n):
            new_assignment = assign(assignment,job)
            if new_assignment:
                lb= lowerbound(new_assignment,C)
                Q.put((lb,new_assignment))

    return optimal

C = [
    [9,2,7,8],
    [6,4,3,7],
    [5,8,1,8],
    [7,6,9,4]
    ]

cost,assignment = findAssignments(C)

print(f"Optimal Solution:-\nAssignment: {assignment}\nCost: {cost}")