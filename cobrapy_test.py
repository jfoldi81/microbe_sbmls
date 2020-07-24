#Jonathan Foldi
#June 13, 2020
#cobrapy test
from __future__ import print_function


import cobra
import cobra.test
import os
from os.path import join
from cobra.util.solver import linear_reaction_coefficients



### "ecoli" and "salmonella" are also valid arguments
##model = cobra.test.create_test_model("textbook")
##
##
##print(len(model.reactions))
##print(len(model.metabolites))
##print(len(model.genes))
##
##print(model.reactions[29])
##
##pgi = model.reactions.get_by_id("PGI")
##print(pgi.name)

#can get specific reactions from searching by metabolite and then getting
# all the reactions in which it's present

#can do the same thing for genes

#MODELS

#can iterate throgh al the reactions of a model and od a knockout of each one
# and see how that affects biomass

# Iterate through the the objects in the model

##print("Reactions")
##print("---------")
##for x in model.reactions:
##    print("%s : %s" % (x.id, x.reaction))
##
##print("")
##print("Metabolites")
##print("-----------")
##for x in model.metabolites:
##    print('%9s : %s' % (x.id, x.formula))
##
##print("")
##print("Genes")
##print("-----")
##for x in model.genes:
##    associated_ids = (i.id for i in x.reactions)
##    print("%s is associated with reactions: %s" %
##          (x.id, "{" + ", ".join(associated_ids) + "}"))


#TEST MODELS
##data_dir = cobra.test.data_dir
##
##print("mini test files: ")
##print(", ".join(i for i in os.listdir(data_dir) if i.startswith("mini")))
##
##textbook_model = cobra.test.create_test_model("textbook")
##ecoli_model = cobra.test.create_test_model("ecoli")
##salmonella_model = cobra.test.create_test_model("salmonella")
##
##model_reactions = (cobra.io.read_sbml_model(join(data_dir, "mini_fbc2.xml")).reactions)
##print(len(model_reactions))

print (os.getcwd())

#set woroking directory to cobrapy folder when importing locally stored files
data_dir = os.getcwd()
print('starting easy here')#so that can find hte start more easily in the shell
easy = cobra.io.read_sbml_model(join(data_dir, "easy.xml"))
##
print(len(easy.reactions),"is how many reactions there are in easy")
easy_solution = easy.optimize()
print(easy_solution,'is the optimized for easy')

#this works!!!



print('starting theta here')
theta = cobra.io.read_sbml_model(join(data_dir, "b-theta.xml"))
print(len(theta.reactions),"is how many reactions there are in theta")
theta_solution = theta.optimize()
print(theta_solution,'is the optimized for theta')

solutions = [easy_solution, theta_solution]
models = ['easy','theta']
model_var = [easy,theta]

for num in range(2):
    print (solutions[num].objective_value,' is the objective value for model ',models[num])
    print (solutions[num].status,' is the status for model ',models[num])
for num in range(2):
    print (model_var[num].summary(),' is the summary for model ',models[num])



#f = open("b-theta.xml", "r")
#print(f.read(100000))
##print(len(theta.reactions))






                                
