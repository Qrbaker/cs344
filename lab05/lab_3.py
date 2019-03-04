"""
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden and qrb2
@version March 2, 2019
"""

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

# P(Raise | Sunny)
print("P(R|S):")
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
print(elimination_ask('Raise', dict(Sunny=T), happy).show_approx())
print(gibbs_ask('Raise', dict(Sunny=T), happy).show_approx())

'''
The probability of a raise is independent on if it is sunny, so the probability of P(R|S) == P(R).
'''

print("===========================================")
# P(Raise | happy ^ sunny)
print("P(R|h^s):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())
print(elimination_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())
print(gibbs_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())
# Result: False: 0.986, True: 0.0142

'''
Manual Solution:

P(R|h^s) = a Σ(P(R|h,s))
         = a * P(s) Σ(P(R|h)
         = 0.7a * <P(R)P(h|R^s), P(-R)P(h|-R^s)>
         = 0.7a * <(0.01)(1), (0.99)(0.7)>
         = 0.7a * <0.01, 0.693>
         (Distribute in 0.7)
         = a * < 0.007, 0.651>
         (Normalizing Constant = 0.007+0.651 = 0.658)
         = <0.007/0.658, 0.651/0.658>
         = <0.1064, 0.9894>
'''

print("===========================================")
# P(Raise | happy)
print("P(R|h):")
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
print(elimination_ask('Raise', dict(Happy=T), happy).show_approx())
print(gibbs_ask('Raise', dict(Happy=T), happy).show_approx())
# Result: False: 0.982, True: 0.0185

'''
This makes sense; it is much more likely to be sunny than to have recieved a raise, so if the agent is happy, its much
more likely its because it is sunny.
'''

print("===========================================")
# P(Raise | happy ^ -sunny)
print("P(R|h^-s):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
print(elimination_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
print(gibbs_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
# Result: False: 0.917, True: 0.0833
'''
Even if it is known that it isn't sunny outside, its still unlikely an agent got a raise, given they are happy (though 
it is *more* likely than the previous example). This is because the likelyhood of just being happy dispite not being 
sunny or having a raise (0.1) is ten times more likely than a raise.
'''
