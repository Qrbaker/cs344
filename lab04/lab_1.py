'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Catch=T)
'''
By-hand method:
Conditional Probability formula: P(A|B) = P(A+B)/P(B)

From what we know:
P(Cavity|Catch) = ((P(Catch|Cavity)P(Cavity))/P(Catch)

P(Catch) = 0.108 + 0.016 + 0.072 + 0.144 = 0.34
P(Cavity && Catch) = 0.108 + 0.072 = 0.18
P(!Cavity && Catch) = 0.016 + 0.144 = 0.16

P(Cavity|Catch) = P(Cavity && Catch)/P(Catch) = (0.18)/0.34 ~= 0.5294
P(!Cavity|Catch) = P(!Cavity && Catch)/P(Catch) = (0.16)/0.34 ~= 0.4706

*P*(Cavity|Catch) = < 0.5294, 0.4706 >
'''

print("Probability distribution of Cavity given Catch:")
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

print("\n==============================================\n")

# Joint Probability Dist. for two coin flips
heads, tails = True, False
C = JointProbDist(["coin1", "coin2"])
C[heads, heads] = 0.25; C[heads, tails] = 0.25
C[tails, heads] = 0.25; C[tails, tails] = 0.25

print("Probability distribution of coin2, given coin1 was heads:\n(False = Tails, True = Heads)")
CC = enumerate_joint_ask('coin2', {'coin1': heads}, C)
print(CC.show_approx())
