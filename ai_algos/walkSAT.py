import random

def walksat(clauses, symbols, p, max_flips):
    model = {x:random.choice([True, False]) for c in clauses for x in c}
    for _ in range(max_flips):
        unsatisfied = [clause for clause in clauses if not any(model.get(x, not x) for x in clause)]

        if not unsatisfied: return model
        
        clause = random.choice(unsatisfied)
        if random.random() < p:
            symbol = random.choice(symbols)
        else:
            symbol = max(clause, key=lambda s: sum(1 for c in unsatisfied if s in c))
        model[symbol] = not model[symbol]
    return None

# clauses should be in CNF: (^A or ^B) and (B or C) and (^C or D)
clauses = [[-1, -2], [2, 3], [-3, 4]]
symbols = [1, 2, 3, 4]
p = 0.5  # probability of flipping a randomly chosen variable
max_flips = 1000

result = walksat(clauses, symbols, p, max_flips)

if result:
    print("Formula is satisfiable.")
    print("Model:", result)
else:
    print("Formula is not satisfiable.")
