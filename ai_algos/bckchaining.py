def backward_chaining(goal, facts, rules):
    for rule in rules:
        if goal in rule["consequence"]:
            if all(fact in facts and facts[fact] for fact in rule["condition"]):
                return True
            else:
                for fact in rule["condition"]:
                    if backward_chaining(fact, facts, rules):
                        return True
    return goal in facts and facts[goal]

rules = []
def addRules(lhs,rhs):
    rules.append({"condition": lhs,"consequence":rhs})

addRules(["P"],["Q"])
addRules(["L","M"],["P"])
addRules(["A","B"],["L"])
addRules(["A","P"],["L"])
addRules(["B","L"],["M"])

facts = {"A": True, "B": True}

# Test the program
print(backward_chaining("L", facts, rules))

