"""
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden and qrb2
@version March 2, 2019
"""

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py)
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
    ])

# P(Cancer | Test1 and Test2 are positive)
print("P(C|T1^T2):")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# Result: False: 0.83, True: 0.17
'''
Even if BOTH tests are positive, the likelyhood the person tested has cancer is still quite low (only ~17%). This comes
down to the fact that dispite the decent spesificity of the tests, in general the likelyhood a given patient has cancer
is just really low (1%).

Manual Solution:
P(C|T1^T2) = a Σ(P(C|t1,t2))
           = a * <(P(C)P(t1|C)P(t2|C), P(-C)P(t1|-C)P(t2|-C)>
           = a <(0.01)(0.9)(0.9), (0.99)(0.2)(0.2)>
           = a <0.0081,0.0396>
           (Normalzing value = 0.0081+0.0396 = 0.0477)
           = <0.0081/0.0477,0.0396/0.0477> 
          -------------------------
           = <0.1698,0.8302>
'''

print("===========================================")
print("P(C|T1^-T2):")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
# Result: False: 0.994, True: 0.00565
'''
If ONE test is positive, but the other is negative, its almost certain the patient does NOT have cancer (> 99%)! This is
because the tests have a low (but non-zero) chance of having a false positive, and the chance of each test's false
positive (10%) is still _an order of magnitude_ more likely than cancer! A person would be justified in assuming the
posttive test was a false positive.

Manual Solution:
P(C|T1^T2) = a Σ(P(C|t1,-t2))
           = a * <(P(C)P(t1|C)P(-t2|C), P(-C)P(t1|-C)P(-t2|-C)>
           = a <(0.01)(0.9)(0.1), (0.99)(0.2)(0.8)>
           = a <0.0009,0.1584>
           (Normalzing value = 0.0009+0.1584 = 0.1593)
           = <0.0009/0.1593,0.1584/0.1593> 
          -------------------------
           = <0.0056,0.9944>
'''
