########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part II - Python Graphs: 2.4
# 
########################################################################

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Create boxplot from random data
dt = [np.random.normal(90, 10, 150), np.random.normal(85, 20, 150), 
      np.random.normal(70, 30, 150)]        # Generate random data

plt.figure(figsize =(10, 10))
plt.boxplot(dt)
plt.title('Boxplot')
plt.show()


