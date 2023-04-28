from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Bayesian network structure
model = BayesianNetwork(
    [
        ("Burglary", "Alarm"), 
        ("Earthquake", "Alarm"), 
        ("Alarm", "JohnCalls"),
        ("Alarm","MaryCalls")]
    )

# CPDs (conditional probability distributions) for each variable
cpd_b = TabularCPD("Burglary", 2, [[0.001], [0.999]])
cpd_e = TabularCPD("Earthquake", 2, [[0.002], [0.998]])
cpd_a = TabularCPD("Alarm", 2, [[0.7, 0.01, 0.7, 0.01], [0.3, 0.99, 0.3, 0.99]], evidence=["Burglary", "Earthquake"], evidence_card=[2, 2])
cpd_j = TabularCPD("JohnCalls", 2, [[0.9, 0.05], [0.1, 0.95]], evidence=["Alarm"], evidence_card=[2])
cpd_m = TabularCPD("MaryCalls", 2, [[0.7, 0.01], [0.3, 0.99]], evidence=["Alarm"], evidence_card=[2])

model.add_cpds(cpd_b, cpd_e, cpd_a, cpd_j,cpd_m)

inference = VariableElimination(model)

# Query for the probability (try to make your own queries)
johnmary_calls_when_notBEA = inference.query(
    variables=["JohnCalls","MaryCalls"], 
    evidence={"Burglary": 0, "Earthquake": 1,"Alarm":1}
    )
print(johnmary_calls_when_notBEA)

alarm_given_burglary_johncalls = inference.query(variables=['Alarm'], evidence={'Burglary': 1, 'JohnCalls': 1})
print(alarm_given_burglary_johncalls)
