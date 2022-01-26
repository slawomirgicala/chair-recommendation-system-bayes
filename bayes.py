from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Defining the network structure
model_ergonomic = BayesianNetwork([('sedentary', 'ergonomic'),
                                   ('earnings', 'ergonomic')])

# Defining the CPDs:
cpd_sedentary = TabularCPD('sedentary', 2, [[0.8], [0.2]], state_names={'sedentary': ['NO', 'YES']})
cpd_earnings = TabularCPD('earnings', 3, [[0.3], [0.5], [0.2]], state_names={'earnings': ['LOW', 'MIDDLE', 'HIGH']})
cpd_ergonomic = TabularCPD('ergonomic', 2, [[1, 0.8, 0.3, 0.99, 0.5, 0.01],
                                            [0, 0.2, 0.7, 0.01, 0.5, 0.99]],
                           evidence=['sedentary', 'earnings'], evidence_card=[2, 3],
                           state_names={'sedentary': ['NO', 'YES'],
                                        'earnings': ['LOW', 'MIDDLE', 'HIGH'],
                                        'ergonomic': ['NO', 'YES']})

# Associating the CPDs with the network structure.
model_ergonomic.add_cpds(cpd_sedentary, cpd_earnings, cpd_ergonomic)

# Variable elimination and prediction
infer = VariableElimination(model_ergonomic)


def ergonomic_probability(evidence):
    return infer.query(['ergonomic'], evidence=evidence, show_progress=False).values[1]
