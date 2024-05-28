from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd
data = pd.DataFrame(data={
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})
model = BayesianNetwork([('Rain', 'TrafficJam'), ('TrafficJam', 'ArriveLate')])
model.fit(data, estimator=MaximumLikelihoodEstimator)
inference = VariableElimination(model)
query_result1= inference.query(variables=['ArriveLate'], evidence={'TrafficJam': 'No'})
print(query_result1)