from itertools import combinations

def resolution(clauses):
    new = set()
    while True:
        for ci,cj in combinations(clauses,2):
            resolvents = resolve(ci, cj)
            if any(len(r) == 0 for r in resolvents): return True
            new.update(resolvents)
        
        if new.issubset(clauses): return False
        clauses.update(new)
        new.clear()

def discard(S,x):
    return frozenset(y for y in S if not y in x)

def resolve(ci, cj):
    resolvents = set()
    u = ci.union(cj)
    for pi in ci:
        for pj in cj:
            if pi == -pj:
                res= discard(u,[pi,pj])
                resolvents.add(res)
    return resolvents

clauses = {frozenset({-1, 2}), frozenset({-2, 3,1}),frozenset({-3, 2}),frozenset({-2,}),frozenset({3,})}

if resolution(clauses): print("Query is proven")
else: print("query is not proven")