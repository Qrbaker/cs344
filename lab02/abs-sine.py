"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def getMaximum(self):
        return self.maximum;

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        # An attempt to limit the search space to positive reals between 0 and 30
        if 0 <= x <= self.maximum:
            return math.fabs(x * math.sin(x))
        else:
            return -(float("inf"))


def test_searches(searchspace):
    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(searchspace)
    print('Hill-climbing solution            x: ' + str(hill_solution)
          + '\t\tvalue: ' + str(p.value(hill_solution))
          )
    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(
        searchspace,
        exp_schedule(k=30, lam=0.005, limit=1000)
    )
    print('Simulated annealing solution      x: ' + str(annealing_solution)
          + '\t\tvalue: ' + str(p.value(annealing_solution))
          )


def test_rr_searches(restarts, initial_max):


    hill_restart_solution = 0
    hill_avg = []
    annealing_restart_solution = 0
    annealing_avg = []
    for i in range(restarts):
        # Get new starting point
        internal_p = SineVariant(randrange(0, initial_max), initial_max, delta=1)

        # Solve using hill-climbing + random restarts
        current_hill_solution = hill_climbing(internal_p)
        hill_avg.append(current_hill_solution)
        if current_hill_solution > hill_restart_solution:
            hill_restart_solution = current_hill_solution

        # Solve the problem using simulated annealing + random restarts
        current_annealing_solution = simulated_annealing(
            internal_p,
            exp_schedule(k=30, lam=0.005, limit=1000)
        )
        annealing_avg.append(current_annealing_solution)
        if current_annealing_solution > annealing_restart_solution:
            annealing_restart_solution = current_annealing_solution

    # Print results of each test
    print('Hill-climbing (RR) solution       x: ' + str(hill_restart_solution)
          + '\t\tvalue: ' + str(internal_p.value(hill_restart_solution))
          + '\taverage of runs: ' + str(sum(hill_avg)/len(hill_avg))
          )

    print('Simulated annealing (RR) solution x: ' + str(annealing_restart_solution)
          + '\t\tvalue: ' + str(internal_p.value(annealing_restart_solution))
          + '\taverage of runs: ' + str(sum(annealing_avg) / len(annealing_avg))
          )


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    r = 10
    maximum = 30
    initial = randrange(0, maximum)
    p = SineVariant(initial, maximum, delta=1)
    print('Initial                           x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    test_searches(p)
    print("=================================================================")
    test_rr_searches(r, maximum)
