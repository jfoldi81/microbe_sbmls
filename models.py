#Jonathan Foldi
#June 20, 2020
#chceking models on cobrapy

import cobra
import cobra.test
import os
from os.path import join
from cobra.util.solver import linear_reaction_coefficients


#set working directory to cobrapy folder when importing locally stored files
data_dir = os.getcwd()
print('starting easy here')#so that can find hte start more easily in the shell
easy = cobra.io.read_sbml_model(join(data_dir, "easy.xml"))
easy_solution = easy.optimize()

#this works!!!



print('starting theta here')

thiele = cobra.io.read_sbml_model(join(data_dir, "theta-thiele.xml"))

thiele_solution = thiele.optimize()
print(thiele_solution,' is the solution to htieele model')
print(len(thiele.reactions),' is how many reactions are in thiele')
print(thiele.summary())
"""

#only changed obkective from id to name
theta = cobra.io.read_sbml_model(join(data_dir, "theta-practice.xml"))
theta_solution = theta.optimize()
solutions = [easy_solution, theta_solution]
models = [easy,theta]

#original doesn't work
original = cobra.io.read_sbml_model(join(data_dir, "b-theta.xml"))
og_sol = original.optimize()
models.append(original)



#swapped all name and id
fixed = cobra.io.read_sbml_model(join(data_dir, "copy.xml"))
fixed_sol = fixed.optimize()#value is 414.369
models.append(fixed)


#final order of models: easy, first, OG, final
for model in models:
    
    print('lineare reaction coeff',linear_reaction_coefficients(model))
    #print first ten reactions of each model
    print(model.reactions[0],' is named ' ,model.reactions[0].name)

print('original solution to theta is: ',og_sol)
print('first solution to theta is: ',theta_solution)
print('final solution to theta is: ',fixed_sol)
"""


