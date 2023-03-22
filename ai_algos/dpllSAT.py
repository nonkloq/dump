def isTrue(clauses,model):
    """
    checking if every clause is true in this partially or fully assigned model 
    """
    for clause in clauses:
        truth = False
        partial = False
        for fact in clause:
            symbol = abs(fact)
            if model[symbol]==None: 
                partial = True
                continue
            if (fact < 0) and not model[symbol]: truth = True 
            elif model[symbol]: truth = True 
        if not partial and not truth: return False
    return True

def find_pure_symbol(symbols, clauses):
    for s in symbols:
        found_in_pos = False
        found_in_neg = False
        for clause in clauses:
            if -s in clause:
                found_in_neg = True
            if s in clause:
                found_in_pos = True
        if found_in_pos != found_in_neg:
            return (s, found_in_pos)
    return (None, None)

def find_unit_clause(clauses,model):
    for x,y in clauses:
        a = abs(x)
        b = abs(y)
        if model[a] != None and model[b] == None and (x<0 and model[a] or not model[a]):
            return (b, False if y<0 else True)
        if model[b] != None and model[a] == None and (y<0 and model[b] or not model[b]): 
            return (a, False if x<0 else True)
    return (None, None)

def remove_symbol(P, symbols):
    symbols.remove(P)
    return symbols

def add_model(P,truth,model):
    model[P]=truth
    return model


def dpll(clauses, symbols, model):
    
    # everything is assigned
    if not symbols: return isTrue(clauses,model)
    # early termination
    if not isTrue(clauses,model): return False
    
    P, value = find_pure_symbol(symbols, clauses)
    if P: return dpll(clauses, remove_symbol(P, symbols), add_model(P,value,model))
    
    P, value = find_unit_clause(clauses,model)
    if P: return dpll(clauses, remove_symbol(P, symbols), add_model(P,value,model))
    P = symbols[0]
    rest = symbols[1:]
    
    return dpll(clauses, rest, add_model(P,True,model)) or \
            dpll(clauses, rest, add_model(P,False,model))

# Clauses should be in CNF: (A or B) and (B or `C) and (C or D)
clauses = [[1, 2], [2, -3], [3, 4]]
symbols = [1, 2, 3, 4]
model = {x: None for x in symbols} # model that satisfy the clauses

result = dpll(clauses, symbols, model)

if result:
    print("Formula is satisfiable.")
    print("Model:", model)
else:
    print("Formula is not satisfiable.")

