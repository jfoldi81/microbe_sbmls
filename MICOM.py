#Jonathan Foldi
#June 21 2020
#MICOM

from micom.data import test_data
from micom import Community
import pandas as pd
import numpy as np
#importing the test community
'''
data = test_data()
print(data['file'][0])
'''

model = pd.read_excel('micom-model.xlsx')
print('up to heere ok')
com = Community(model)
print("Build a community")
print(com.taxonomy)

print(com.objective.expression)
sol = com.optimize(fluxes=True, pfba=True)
print(sol,' is the optimized objective')



#can't do yet bc wrong solver
sols = com.cooperative_tradeoff(fraction=np.arange(0.1, 1.01, 0.1))
print(sols)
 
