########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part II - Python Graphs: 2.2
# 
########################################################################

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Create a bar plot with random data
x = np.arange(10)       # Define x
y = np.random.randint(0,20,10)  # Define y

# Plot figure
plt.figure()
plt.bar(x, y)
plt.xlabel('Numbers')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()
plt.clf()

# Create a pie chart
labels = ['A', 'B', 'C', 'D', 'E', 'F']
 
data = [5, 13, 30, 23, 12, 17]
 
# Creating pie plot
plt.figure()
plt.pie(data, labels = labels)
plt.title('Pie Plot')
plt.show()