"""
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden and qrb2
@version March 1, 2019
"""

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])


'''Each probability is found (or an attempt to find it is made, at least...) with three different methods: 
1. Enumeration ask, which is the classic 'brute force' method. It will loop through all possible values, and compute the
   probability for each one. For this simple version, it isn't noticable, but this method will start to take noticably 
   longer with more complex networks. The upside is that it will _always_ (eventually) produce a result. 

2. Elimination ask (a.k.a variable elimination), a dynamic programming optimization of the above algorithm, that first 
   tries to compute basic probabilities and _then_ computing the dependent probabilities, repeating and simplifying 
   until our input expression is only in terms of the variable(s) we're looking for. If this succeeds, it will have an
   identical result as 1.
   
3. Gibbs sampling, which unlike the previous algorithms, produces an estimate, rather than an exact value. It is a 
   stochastic process (spesifically Monte Carlo Markov Chain, or MCMC) that will converge on the correct actual 
   probability over n iterations.
'''

# --- P(Alarm | burglary and not earthquake) --- #
print("P(A|b^-e):")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# Result: False: 0.06, True: 0.94
'''
According to the results, if there has been a burglary, but not an earthquake, the alarm will almost certainly go off 
(~95%). This makes sense, as any effective security solution will be designed to detect a burglary as best as it can. 
'''

print("===========================================")
# --- P(John calls | burglary and not earthquake) --- #
print("P(J|b^-e):")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# Result: False: 0.151, True: 0.849

'''
According to the results, if there has been a burglary, it is fairly likely John calls (~85%). However, there is a 
decent non-zero chance he will NOT call as well. This intuitively makes sense, as John is a human, and thus could be 
asleep, or not home, or just wouldn't hear the alarm for some reason. Additionally, this stacks with the slim chance 
that the alarm may also simply not go off, as calculated above. 
'''

print("===========================================")
# --- P(Burglary | alarm) --- #
print("P(B|a):")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# False: 0.626, True: 0.374

'''
Given how unlikely a burglary is (< 1%), even though an alarm rarely goes off its generally _more likely_ to be a "false
positive" (~60%) than an actual burglary. The results are therefore within expectations.
'''

print("===========================================")
# --- P(Burglary | John and Mary both call) --- #
print("P(B|j^m):")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# Result: False: 0.716, True: 0.284

'''
If BOTH John and Mary call, it is likely there has been a burglary (~70%). However, there are many reasons both John and
Mary might call aside from an alarm going off (its even possible that one calling is not independent of the other), and 
the alarm going off does not mean a burglary is certain. 

Mary is generally less likely to call if there is a burglary than John, but John is also more likely to call if there 
isn't a burglary. These together cause the probability to be lower.
'''
