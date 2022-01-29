from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Defining the network structure
model_ergonomic = BayesianNetwork([('sedentary', 'active'),
                                   ('weightlifting', 'active'),
                                   ('cardio', 'active'),
                                   ('yoga', 'active'),
                                   ('sedentary', 'hump'),
                                   ('weightlifting', 'hump'),
                                   ('height', 'hump'),
                                   ('height', 'scoliosis'),
                                   ('active', 'scoliosis'),
                                   ('weight', 'obesity'),
                                   ('active', 'obesity'),
                                   ('scoliosis', 'bad_posture'),
                                   ('hump', 'bad_posture'),
                                   ('bad_posture', 'ergonomic'),
                                   ('earnings', 'ergonomic')])

# Defining the CPDs:
# inputs
cpd_sedentary = TabularCPD('sedentary', 2, [[0.8], [0.2]], state_names={'sedentary': ['NO', 'YES']})
cpd_weightlifting = TabularCPD('weightlifting', 2, [[0.9], [0.1]], state_names={'weightlifting': ['NO', 'YES']})
cpd_cardio = TabularCPD('cardio', 2, [[0.75], [0.25]], state_names={'cardio': ['NO', 'YES']})
cpd_yoga = TabularCPD('yoga', 2, [[0.95], [0.05]], state_names={'yoga': ['NO', 'YES']})
cpd_height = TabularCPD('height', 3, [[0.25], [0.6], [0.15]], state_names={'height': ['SHORT', 'MIDDLE', 'TALL']})
cpd_weight = TabularCPD('weight', 3, [[0.25], [0.6], [0.15]], state_names={'weight': ['SLIM', 'NORMAL', 'FAT']})
cpd_sex = TabularCPD('sex', 2, [[0.5], [0.5]], state_names={'sex': ['MALE', 'FEMALE']})
cpd_married = TabularCPD('married', 2, [[0.4], [0.6]], state_names={'married': ['NO', 'YES']})
cpd_offspring = TabularCPD('offspring', 3, [[0.5], [0.3], [0.2]], state_names={'offspring': ['NO', 'ONE', 'MANY']})
cpd_age = TabularCPD('age', 3, [[0.25], [0.6], [0.15]], state_names={'weight': ['YOUNG', 'MEDIUM', 'OLD']})
cpd_doctor = TabularCPD('doctor', 2, [[0.99], [0.01]], state_names={'doctor': ['NO', 'YES']})
cpd_programmer = TabularCPD('programmer', 2, [[0.9], [0.1]], state_names={'programmer': ['NO', 'YES']})
cpd_lawyer = TabularCPD('lawyer', 2, [[0.92], [0.08]], state_names={'lawyer': ['NO', 'YES']})
cpd_fisherman = TabularCPD('fisherman', 2, [[0.79], [0.21]], state_names={'fisherman': ['NO', 'YES']})
cpd_traveller = TabularCPD('traveller', 2, [[0.6], [0.4]], state_names={'traveller': ['NO', 'YES']})

# 1 level
cpd_active = TabularCPD('active', 2,
                        [[1, 0.85, 0.55, 0.75, 0.8, 0.63, 0.5, 0.6, 0.3, 0.2, 0.12, 0.1, 0.07, 0.06, 0.05, 0],
                         [0, 0.15, 0.45, 0.25, 0.2, 0.37, 0.5, 0.4, 0.7, 0.8, 0.88, 0.9, 0.93, 0.94, 0.95, 1]],
                        evidence=['sedentary', 'weightlifting', 'cardio', 'yoga'], evidence_card=[2, 2, 2, 2],
                        state_names={'sedentary': ['NO', 'YES'],
                                     'weightlifting': ['NO', 'YES'],
                                     'cardio': ['NO', 'YES'],
                                     'yoga': ['NO', 'YES'],
                                     'active': ['NO', 'YES']})

cpd_hump = TabularCPD('hump', 2, [[0.3, 0.85, 0.23, 0.81, 0.8, 0.63, 0.4, 0.6, 0.2, 0.2, 0.12, 0.1],
                                  [0.7, 0.15, 0.77, 0.19, 0.2, 0.37, 0.6, 0.4, 0.8, 0.8, 0.88, 0.9]],
                      evidence=['sedentary', 'weightlifting', 'height'], evidence_card=[2, 2, 3],
                      state_names={'sedentary': ['NO', 'YES'],
                                   'weightlifting': ['NO', 'YES'],
                                   'height': ['SHORT', 'MIDDLE', 'TALL'],
                                   'hump': ['NO', 'YES']})

cpd_scoliosis = TabularCPD('scoliosis', 2, [[0.95, 0.85, 0.23, 0.17, 0.8, 0.01],
                                            [0.05, 0.15, 0.77, 0.83, 0.2, 0.99]],
                           evidence=['height', 'active'], evidence_card=[3, 2],
                           state_names={'height': ['SHORT', 'MIDDLE', 'TALL'],
                                        'active': ['NO', 'YES'],
                                        'scoliosis': ['NO', 'YES']})

cpd_obesity = TabularCPD('obesity', 2, [[0.95, 0.85, 0.23, 0.17, 0.8, 0.01],
                                        [0.05, 0.15, 0.77, 0.83, 0.2, 0.99]],
                         evidence=['weight', 'active'], evidence_card=[3, 2],
                         state_names={'weight': ['SLIM', 'NORMAL', 'FAT'],
                                      'active': ['NO', 'YES'],
                                      'obesity': ['NO', 'YES']})

cpd_bad_posture = TabularCPD('bad_posture', 2, [[0.95, 0.85, 0.8, 0.01],
                                                [0.05, 0.15, 0.2, 0.99]],
                             evidence=['hump', 'scoliosis'], evidence_card=[2, 2],
                             state_names={'hump': ['NO', 'YES'],
                                          'scoliosis': ['NO', 'YES'],
                                          'bad_posture': ['NO', 'YES']})

cpd_earnings = TabularCPD('earnings', 3, [[0.3], [0.5], [0.2]], state_names={'earnings': ['LOW', 'MIDDLE', 'HIGH']})
cpd_ergonomic = TabularCPD('ergonomic', 2, [[1, 0.8, 0.3, 0.99, 0.5, 0.01],
                                            [0, 0.2, 0.7, 0.01, 0.5, 0.99]],
                           evidence=['bad_posture', 'earnings'], evidence_card=[2, 3],
                           state_names={'bad_posture': ['NO', 'YES'],
                                        'earnings': ['LOW', 'MIDDLE', 'HIGH'],
                                        'ergonomic': ['NO', 'YES']})

# Associating the CPDs with the network structure.
model_ergonomic.add_cpds(cpd_sedentary, cpd_weightlifting, cpd_cardio, cpd_yoga, cpd_active, cpd_hump, cpd_height,
                         cpd_scoliosis, cpd_weight, cpd_obesity, cpd_bad_posture, cpd_earnings, cpd_ergonomic)

# Variable elimination and prediction
infer = VariableElimination(model_ergonomic)

print(model_ergonomic.get_cpds('ergonomic'))


def ergonomic_probability(evidence):
    return infer.query(['ergonomic'], evidence=evidence, show_progress=False).values[1]
