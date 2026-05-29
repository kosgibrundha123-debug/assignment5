from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# Create Bayesian Network
model = DiscreteBayesianNetwork([
    ("Disease", "Fever"),
    ("Disease", "Cough"),
    ("Disease", "Fatigue")
])


cpd_disease = TabularCPD(
    variable="Disease",
    variable_card=2,
    values=[[0.7], [0.3]]
)

cpd_fever = TabularCPD(
    variable="Fever",
    variable_card=2,
    values=[
        [0.8, 0.2],
        [0.2, 0.8]
    ],
    evidence=["Disease"],
    evidence_card=[2]
)

cpd_cough = TabularCPD(
    variable="Cough",
    variable_card=2,
    values=[
        [0.7, 0.3],
        [0.3, 0.7]
    ],
    evidence=["Disease"],
    evidence_card=[2]
)

cpd_fatigue = TabularCPD(
    variable="Fatigue",
    variable_card=2,
    values=[
        [0.9, 0.4],
        [0.1, 0.6]
    ],
    evidence=["Disease"],
    evidence_card=[2]
)


# Add probability tables
model.add_cpds(
    cpd_disease,
    cpd_fever,
    cpd_cough,
    cpd_fatigue
)


print("Bayesian Network Model")
print("Nodes:", model.nodes())
print("Edges:", model.edges())

print("\nChecking Model...")
print("Model Valid:", model.check_model())


# Perform inference
inference = VariableElimination(model)

print("\nSymptoms Given:")
print("Fever = Yes")
print("Cough = Yes")

result = inference.query(
    variables=["Disease"],
    evidence={
        "Fever": 1,
        "Cough": 1
    }
)

print("\nInference Result:")
print(result)

print("\nInterpretation:")
print("The Bayesian Network predicts")
print("the probability of disease")
print("based on given symptoms.")

print("\nSymptoms used in prediction:")
print("- Fever")
print("- Cough")
print("- Fatigue")
