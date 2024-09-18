import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for CO1, Lecture Rating, Appropriateness, and Result
co1 = ctrl.Antecedent(np.arange(0, 5, 1), 'CO1')
lecture_rating = ctrl.Antecedent(np.arange(0, 4, 1), 'Lecture Rating')
appropriateness = ctrl.Antecedent(np.arange(0, 2, 1), 'Appropriateness Of Assessment Tools')
result_for_course = ctrl.Consequent(np.arange(0, 11, 1), 'Result')

# Define fuzzy membership functions
co1['low'] = fuzz.trimf(co1.universe, [0, 1, 2.5])
co1['medium'] = fuzz.trimf(co1.universe, [1, 2.5, 4])
co1['high'] = fuzz.trimf(co1.universe, [2.5, 4, 5])

lecture_rating['poor'] = fuzz.trimf(lecture_rating.universe, [0, 0, 1])
lecture_rating['average'] = fuzz.trimf(lecture_rating.universe, [0, 1, 2])
lecture_rating['good'] = fuzz.trimf(lecture_rating.universe, [1, 2, 3])
lecture_rating['excellent'] = fuzz.trimf(lecture_rating.universe, [2, 3, 3])

appropriateness['not_appropriate'] = fuzz.trimf(appropriateness.universe, [0, 0, 1])
appropriateness['appropriate'] = fuzz.trimf(appropriateness.universe, [0, 1, 1])

result_for_course['low'] = fuzz.trimf(result_for_course.universe, [0, 0, 5])
result_for_course['medium'] = fuzz.trimf(result_for_course.universe, [0, 5, 10])
result_for_course['high'] = fuzz.trimf(result_for_course.universe, [5, 10, 10])

# Define fuzzy rules
rule1 = ctrl.Rule(co1['high'] & lecture_rating['good'] & appropriateness['appropriate'], result_for_course['high'])
rule2 = ctrl.Rule(co1['low'] & lecture_rating['poor'] & appropriateness['not_appropriate'], result_for_course['low'])

# Create control system and simulation
result_ctrl = ctrl.ControlSystem([rule1, rule2])
result_sim = ctrl.ControlSystemSimulation(result_ctrl)  # Changed to use result_ctrl

# Provide input values
result_sim.input['CO1'] = 4
result_sim.input['Lecture Rating'] = 2
result_sim.input['Appropriateness Of Assessment Tools'] = 1  # Binary input: either 0 (not appropriate) or 1 (appropriate)

# Compute output
result_sim.compute()

# Print output
print(f"Result for course: {result_sim.output['Result']}")

