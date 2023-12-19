########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part III - Basic Statistics and Probability Using Python: 3.7
# 
########################################################################

# Import libraries
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson
from numpy import random


# 3.7.1 

# 3.1. Solve Binomial Distribution
# Calculate probability
b_0 = binom.pmf(k=0, n=12, p=0.2)       # Calculate P(X=0)
b_1 = binom.pmf(k=1, n=12, p=0.2)       # Calculate P(X=1)
b_2 = binom.pmf(k=2, n=12, p=0.2)       # Calculate P(X=2)
b_3 = binom.pmf(k=3, n=12, p=0.2)       # Calculate P(X=3)
b_4 = binom.pmf(k=4, n=12, p=0.2)       # Calculate P(X=4)

# Calculate total probability
b_tot = b_0 + b_1 + b_2 + b_3 + b_4     # Calculate P(X=0)+...+P(X=4)

# Convert probability to %
b_tot = b_tot * 100

# Print result of 3.1
print('3.1 Answer ---> Probability = %.1f' %b_tot)
print('\n')


# 3.7.2

# 3.1 Plot Binomial Distribution & save plot
random.seed(42) 
x = random.binomial(n=12, p=0.2, size=1000)

plt.figure(figsize=(10, 8))
plt.hist(x, bins = 20, color='g', density=True, edgecolor='black')
plt.title('3.7.2 Binomial Distribution')
plt.savefig('3.7.2 Binomial Distribution.png')
plt.savefig('3.7.2 Binomial Distribution.svg')          
plt.savefig('3.7.2 Binomial Distribution.jpeg')
plt.savefig('3.7.2 Binomial Distribution.pdf') 
plt.clf()


# 3.7.1

# 3.2 Solve Poisson Distribution
# Calculate probability
p = []                                  # Create empty list

for i in range(17):                     # Use for loop to calculate sum (p(x=0)+....+p(x=16))
    p_less = poisson.pmf(k=i, mu=12)
    p.append(p_less)

# Calculate total probability
p_tot = 1 - sum(p)                      # Caculate 1-((p(x=0)+...+p(x=16)))

# Convert probability to %
p_tot = p_tot * 100

# Print result of 3.2
print('3.2 Answer ---> Probability = %.1f' %p_tot)
print('\n')


# 3.7.2

# 3.2 Plot Poisson Distribution & save plot
x = poisson.rvs(mu=12, size=1000)

plt.figure(figsize=(10, 8))
plt.hist(x, bins = 20, color='purple', density=True, edgecolor='black')
plt.title('3.7.2 Poisson Distribution')
plt.savefig('3.7.2 Poisson Distribution.png')
plt.savefig('3.7.2 Poisson Distribution.svg')
plt.savefig('3.7.2 Poisson Distribution.jpeg')
plt.savefig('3.7.2 Poisson Distribution.pdf')
plt.clf()