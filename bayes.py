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
                                   ('earnings', 'ergonomic'),
                                   ('doctor', 'budget'),
                                   ('lawyer', 'budget'),
                                   ('programmer', 'budget'),
                                   ('age', 'residence'),
                                   ('budget', 'residence'),
                                   ('traveller', 'residence'),
                                   ('married', 'residence'),
                                   ('programmer', 'business_owner'),
                                   ('age', 'business_owner'),
                                   ('married', 'business_owner'),
                                   ('doctor', 'business_owner'),
                                   ('age', 'baby_chair'), 
                                   ('married', 'baby_chair'),
                                   ('traveller', 'baby_chair'),
                                   ('business_owner', 'leasing'),
                                   ('traveller', 'leasing'),
                                   ('bad_posture', 'leasing'),
                                   ('angler', 'travel_chair'),
                                   ('traveller', 'travel_chair'),
                                   ])

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
cpd_age = TabularCPD('age', 3, [[0.25], [0.6], [0.15]], state_names={'age': ['YOUNG', 'MEDIUM', 'OLD']})
cpd_doctor = TabularCPD('doctor', 2, [[0.99], [0.01]], state_names={'doctor': ['NO', 'YES']})
cpd_programmer = TabularCPD('programmer', 2, [[0.9], [0.1]], state_names={'programmer': ['NO', 'YES']})
cpd_lawyer = TabularCPD('lawyer', 2, [[0.92], [0.08]], state_names={'lawyer': ['NO', 'YES']})
cpd_angler = TabularCPD('angler', 2, [[0.79], [0.21]], state_names={'angler': ['NO', 'YES']})
cpd_traveller = TabularCPD('traveller', 2, [[0.6], [0.4]], state_names={'traveller': ['NO', 'YES']})
cpd_earnings = TabularCPD('earnings', 3, [[0.3], [0.5], [0.2]], state_names={'earnings': ['LOW', 'MIDDLE', 'HIGH']})

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

cpd_ergonomic = TabularCPD('ergonomic', 2, [[1, 0.8, 0.3, 0.99, 0.5, 0.01],
                                            [0, 0.2, 0.7, 0.01, 0.5, 0.99]],
                           evidence=['bad_posture', 'earnings'], evidence_card=[2, 3],
                           state_names={'bad_posture': ['NO', 'YES'],
                                        'earnings': ['LOW', 'MIDDLE', 'HIGH'],
                                        'ergonomic': ['NO', 'YES']})

cpd_budget = TabularCPD('budget', 3,
                        [[0.6, 0.4, 0.3, 0.15, 0.1, 0.0, 0.0, 0.0],
                         [0.4, 0.3, 0.3, 0.25, 0.2, 0.1, 0.05, 0.0],
                         [0.0, 0.3, 0.4, 0.6, 0.7, 0.9, 0.95, 1.0]],
                        evidence=['doctor', 'lawyer', 'programmer'], evidence_card=[2, 2, 2],
                        state_names={'doctor': ['NO', 'YES'],
                                     'lawyer': ['NO', 'YES'],
                                     'programmer': ['NO', 'YES'],
                                     'yoga': ['NO', 'YES'],
                                     'budget': ['LOW', 'MEDIUM', 'HIGH']})

cpd_residence = TabularCPD('residence', 4,
                        [
                           [0.74, 0.42, 0.16, 0.06, 0.07, 0.21, 0.49, 0.0, 0.46, 0.07, 0.06, 0.04, 0.47, 0.26, 0.47, 0.19, 0.22, 0.03, 0.22, 0.01, 0.05, 0.13, 0.3, 0.12, 0.03, 0.17, 0.6, 0.53, 0.32, 0.0, 0.46, 0.05, 0.06, 0.15, 0.29, 0.46],
                           [0.01, 0.18, 0.49, 0.48, 0.21, 0.21, 0.05, 0.46, 0.33, 0.35, 0.51, 0.49, 0.4, 0.59, 0.09, 0.08, 0.25, 0.28, 0.06, 0.04, 0.16, 0.02, 0.15, 0.03, 0.27, 0.17, 0.08, 0.27, 0.41, 0.36, 0.12, 0.18, 0.01, 0.69, 0.09, 0.21],
                           [0.22, 0.09, 0.28, 0.4, 0.17, 0.1, 0.2, 0.11, 0.07, 0.52, 0.01, 0.28, 0.01, 0.13, 0.06, 0.15, 0.14, 0.6, 0.33, 0.85, 0.61, 0.78, 0.4, 0.81, 0.11, 0.56, 0.17, 0.19, 0.03, 0.08, 0.08, 0.21, 0.69, 0.08, 0.01, 0.15],
                           [0.03, 0.31, 0.06, 0.06, 0.55, 0.48, 0.26, 0.44, 0.14, 0.07, 0.42, 0.19, 0.12, 0.01, 0.37, 0.57, 0.39, 0.09, 0.39, 0.09, 0.18, 0.07, 0.15, 0.04, 0.59, 0.1, 0.14, 0.01, 0.24, 0.55, 0.34, 0.56, 0.24, 0.08, 0.6, 0.18]
                        ],
                        evidence=['age', 'budget', 'married', 'traveller'], evidence_card=[3, 3, 2, 2],
                        state_names={'age' : ['YOUNG', 'MEDIUM', 'OLD'],
                                     'budget': ['LOW', 'MEDIUM', 'HIGH'],
                                     'married': ['NO', 'YES'],
                                     'traveller': ['NO', 'YES'],
                                     'residence': ['parents', 'permament', 'rental', 'temporary']})

cpd_business_owner = TabularCPD('business_owner', 2,
                        [
                            [0.49, 0.28, 0.34, 0.11, 0.7, 0.34, 0.21, 0.2, 0.53, 0.14, 0.62, 0.02, 0.28, 0.9, 0.07, 0.12, 0.37, 0.23, 0.08, 0.07, 0.83, 0.5, 0.72, 0.6],
                            [0.51, 0.72, 0.66, 0.89, 0.3, 0.66, 0.79, 0.8, 0.47, 0.86, 0.38, 0.98, 0.72, 0.1, 0.93, 0.88, 0.63, 0.77, 0.92, 0.93, 0.17, 0.5, 0.28, 0.4]
                        ],
                        evidence=['age', 'programmer', 'married', 'doctor'], evidence_card=[3, 2, 2, 2],
                        state_names={'age' : ['YOUNG', 'MEDIUM', 'OLD'],
                                     'programmer': ['NO', 'YES'],
                                     'married': ['NO', 'YES'],
                                     'doctor': ['NO', 'YES'],
                                     'business_owner':['NO', 'YES']})

cpd_baby_chair = TabularCPD('baby_chair', 2,
                        [
                            [0.28, 0.72, 0.07, 0.19, 0.19, 0.72, 0.69, 0.2, 0.19, 0.35, 0.01, 0.76],
                            [0.72, 0.28, 0.93, 0.81, 0.81, 0.28, 0.31, 0.8, 0.81, 0.65, 0.99, 0.24]
                        ],
                        evidence=['age', 'married', 'traveller'], evidence_card=[3, 2, 2],
                        state_names={'age' : ['YOUNG', 'MEDIUM', 'OLD'],
                                     'traveller': ['NO', 'YES'],
                                     'married': ['NO', 'YES'],
                                     'baby_chair':['NO', 'YES']})

cpd_leasing = TabularCPD('leasing', 2,
                        [
                            [1, 1, 0.7, 0.19, 0.01, 0.9, 0.4, 0.8],
                            [0, 0, 0.3, 0.81, 0.99, 0.1, 0.6, 0.2]
                        ],
                        evidence=['business_owner', 'traveller', 'bad_posture'], evidence_card=[2, 2, 2],
                        state_names={'traveller': ['NO', 'YES'],
                                     'business_owner': ['NO', 'YES'],
                                     'bad_posture' : ['NO', 'YES'],
                                     'leasing':['NO', 'YES']})

cpd_travel_chair = TabularCPD('travel_chair', 2,
                        [
                            [0.8, 0.1, 0.1, 0],
                            [0.2, 0.9, 0.9, 1]
                        ],
                        evidence=['traveller', 'angler'], evidence_card=[2, 2],
                        state_names={'traveller': ['NO', 'YES'],
                                     'angler': ['NO', 'YES'],
                                     'travel_chair':['NO', 'YES']})

# Associating the CPDs with the network structure.
model_ergonomic.add_cpds(cpd_sedentary, cpd_weightlifting, cpd_cardio, cpd_yoga, cpd_active, cpd_hump, cpd_height,
                         cpd_scoliosis, cpd_weight, cpd_obesity, cpd_bad_posture, cpd_earnings, cpd_ergonomic, cpd_budget,
                         cpd_doctor, cpd_lawyer, cpd_programmer, cpd_age, cpd_married, cpd_traveller, cpd_residence, cpd_business_owner,
                         cpd_baby_chair, cpd_leasing, cpd_travel_chair, cpd_angler, cpd_travel_chair)

# Variable elimination and prediction
infer = VariableElimination(model_ergonomic)

def model_probabilites(evidence, categories=['ergonomic']):
    results = {}

    q = infer.query(categories, evidence=evidence, show_progress=False)
    rounded = [round(x,2) for x in q.values] 

    for c in categories:
        results[c] = dict(zip(q.state_names[c], rounded))
    
    return results
