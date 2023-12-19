########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part II - Python Graphs: 2.1
# 
########################################################################

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import random

# Define function to draw random line plot
def draw_lp(sb):
    """Draw random line graph."""
    
    # Create x & y data points
    x = np.sort(np.random.randint(low=0, high=20, size=20))
    y = np.random.randint(low=0, high=20, size=20)
    
    # plotting the line
    sb.plot(x, y, label = 'line')
    
    # naming the x axis
    sb.set_xlabel('x')
    
    # naming the y axis
    sb.set_ylabel('y')
    
    # giving a title to my graph
    sb.set_title('Line graph')
    
    # show a legend on the plot
    sb.legend()
    
# Plot 1x2 graph
plt.figure(figsize=(14, 7))         # Set figue size

for i in range(2):                  # Call function to draw 1x2 plot
    sb = plt.subplot(1, 2, i+1)
    draw_lp(sb)
    
plt.show()                          # Show the plot
plt.clf()


# Plot 2x2 graph
plt.figure(figsize=(14, 14))         # Set figue size

for i in range(4):                  # Call function to draw 1x2 plot
    sb = plt.subplot(2, 2, i+1)
    draw_lp(sb)
    
plt.show()                          # Show the plot
plt.clf()


# Plot 4x4 graph
plt.figure(figsize=(20, 20))         # Set figue size

for i in range(16):                  # Call function to draw 1x2 plot
    sb = plt.subplot(4, 4, i+1)
    draw_lp(sb)
    
plt.show()                          # Show the plot
plt.clf()