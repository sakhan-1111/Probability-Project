########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part II - Python Graphs: 2.3
# 
########################################################################

# Import libraries
import matplotlib.pyplot as plt
import random

# Plot histogram with random data
dt = [random.randint(1, 100) for x in range(100)]
plt.hist(dt, bins=15)
plt.title('Histogram plot')
plt.show()