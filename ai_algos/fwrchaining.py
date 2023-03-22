def forward_chaining(facts, rules):
    new_facts = facts.copy()
    queue = [fact for fact in facts if facts[fact]==True]
    while queue:
        fact = queue.pop(0)
        for rule in rules:
            if fact in rule["condition"] and all(f in new_facts and new_facts[f] for f in rule["condition"]):
                for consequence in rule["consequence"]:
                    if consequence not in new_facts:
                        new_facts[consequence] = True
                        queue.append(consequence)
    return new_facts

rules = []
def addRules(lhs,rhs):
    rules.append({"condition": lhs,"consequence":rhs})

addRules(["P"],["Q"])
addRules(["L","M"],["P"])
addRules(["A","B"],["L"])
addRules(["A","P"],["L"])
addRules(["B","L"],["M"])

facts = {"A": True, "B": True}

print(forward_chaining(facts, rules))

