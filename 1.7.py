########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part I - Python Basics: 1.7
# 
########################################################################

# Import libraries
import numpy as np
from random import seed
from random import randint

# 1.7.1 Create a 4x4 matrix A
A = np.array([[1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [4, 4, 4, 4]])

# Print matrix A
print('1.7.1 4x4 Matrix A = \n', A)


# 1.7.2 Create a 1x4 matrix B
B = np.array([[1, 1, 1, 1]])


# Print matrix B
print('\n1.7.2 1x4 Matrix B = \n', B)


# 1.7.3 Create a 4x1 matrix C
C = np.array([[1],
              [2],
              [3],
              [4]])

# Print matrix C
print('\n1.7.3 4x1 Matrix C = \n', C)


# 1.7.4 Combine (column) A and B
A_B_column = np.concatenate((A, B), axis=0)

# Print matrix A_B_column
print('\n1.7.4 Matrix A_B_column = \n', A_B_column)


# 1.7.5 Combine (row) A and C
A_C_row = np.concatenate((A, C), axis=1)

# Print matrix A_C_row
print('\n1.7.5 Matrix A_C_row = \n', A_C_row)


# 1.7.6 Create an array (1x20) with all random values (an integer between 0 and 9) and name it x.
# Set random seed value
seed(42)

# Create an empty list
x = []

# generate 20 random numbers 0-9 
for s in range(20):
    value = randint(0, 9)
    x.append(value)

# Convert x to numpy array
x = np.array([x])

# Print array x
print('\n1.7.6 Array x = \n', x)


# 1.7.7 Write a function to calculate mean, standard deviation, max, min, and median of a list.
# Test list
numbers = [1, 4, 9, 5, 3, 2]

# Define function to perform opertaions
def op(num):
    # Calculate mean
    mean = sum(num)/len(num)
    
    # Calculate variance
    variance = sum([((x - mean) ** 2) for x in num]) / len(num)
    
    # Calculate standard deviation
    sd = variance ** 0.5
    
    # Calculate max
    mx = max(num)
    
    # Calculate min
    mn = min(num)
    
    # Sort the input
    num.sort()
    
    # Calculate median
    mid = len(num) // 2
    md = (num[mid] + num[~mid]) / 2
    
    # Print result
    return print('Mean = ' + str(mean) + '\n',
                 'Standard Deviation = ' + str(sd) + '\n',
                 'Max = ' + str(mx) + '\n',
                 'Min = ' + str(mn) + '\n',
                 'Median = ' + str(md) + '\n')

# Call function to perform operation
print('\n1.7.7 Calling function to perform mean, standard deviation, max, min, and median of list \n', numbers)
op(numbers)