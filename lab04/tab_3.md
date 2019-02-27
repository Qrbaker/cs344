*Note: This document is written in Markdown syntax. Answers to questions are _underlined_.*

## a) Drug Testing

### Given Info: 

* P(T|U) = 0.99
* P(-T|-U) = 0.98
* P(U) = 0.089 (And therefore, P(-U) = 1 - 0.089 = 0.911)

### Joint Probability Table:
     |Test |-Test
-----|-----|-------
User |0.088|0.00089
-User|0.018|0.893  	  
				 
	
### Problems:

	i. **P**(User) = ?
		
		**P**(U) = _<0.089, 0.911>_
		
	ii. P(Test|User) = ?
		
		P(T|U) = _0.99_
		
	iii. P(-Test|User) = ?
		
		P(-T|U) = 1 - P(T|U) = 1 - 0.99 = _0.01_
		
	iv. P(Test|-User) = ?
		
		P(T|-U) = P(T^-U) / P(-U) = 0.018 / 0.911 = 0.02
	
	v. **P**(User|Test) = ?
	
		P(U|T) = P(U^T) / P(T) = 0.088 / (0.088 + 0.018) = 0.83
		
		**P**(U|T) = _<0.83, 0.17>_
		
## b) Breast Cancer

### Given Info:

* P(C) = 0.01
* P(T|C) = 0.80
* P(T|-C) = 0.096

### Joint Probability Table
	
     |Cancer|-Cancer
-----|------|-------
Test | .008 |.095
-Test| .002 |0.89

A woman in this age group is found to have a positive mammography in a routine screening. What are the chances that she has/doesn't have cancer?

* P (C|T) = ?

P (C|T) = P(C^T) / P(T)

		= 0.008 / (0.008 + 0.095) = 0.008 / 0.103 = _0.0777_, or _7%_ chance this patience has cancer.