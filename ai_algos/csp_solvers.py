def AC3(csp):
    """
    AC3 arc concistency checker
    Input: csp = (constraint Graph map: dict, variable to Domain map: dict)
    Output: True if the given csp is solvable else False
    """
    graph,D = csp
    assignments = {}

    Q = [(u,v) for u,adj in graph.items() for v in adj]

    while Q:
        Xi, Xj = Q.pop(0)
        if revise(Xi, Xj,assignments,D):
            if len(D[Xi]) == 0: return False
            
            for Xk in graph[Xi]:
                if Xk == Xj: continue
                Q.append((Xk, Xi))

        elif len(D[Xi]) > 0: 
            assignments[Xi] = D[Xi][0] # assigning an arbitrary domain value

    return True

def revise( Xi, Xj,assignments,D):
    revised = False
    for x in D[Xi]:
        if Xj in assignments and x in assignments[Xj]:
            D[Xi].remove(x) 
            revised = True
    
    return revised

def BacktrackingSearch(csp,inference):
    """
    Input:  csp = (variables: list, domain: list)
            inference = function that perform defined inference on the assignment
    Output: assignment if the given csp is solvable else None
    """
    variables,domain = csp 

    def Backtrack(assignment):
        if len(assignment) == len(variables): return assignment
        var = [v for v in variables if v not in assignment][0]
    
        for value in domain:
            assignment[var] = value
            if inference(assignment):
                result = Backtrack(assignment)
                if result: return result
            assignment.pop(var)
        
        return None

    return Backtrack({})
