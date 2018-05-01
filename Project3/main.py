"""
This script is the main executable of my recommender system. See the included
documentation files for details about how to use the program and how to
interpret the results.
    Created By:     Joseph Allen
    Date:           3/25/2018
"""

from gui import *
from problem import *
from solver import *

attributes,constraints,preferences = gui()

problem = Problem(attributes, constraints, preferences)
problem.getAttributes()
problem.getConstraints()
problem.getPreferences()
problem.writeConstraints()

solver = Solver(problem)
solver.runClasp()
solver.getFeasibleModels()
solver.whichLogic()
solver.calculatePreferences()
solver.twoRandomModels()
solver.optimization()
solver.omniOptimization()
solver.toString()