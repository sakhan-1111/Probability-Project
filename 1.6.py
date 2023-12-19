########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part I - Python Basics: 1.6
# 
########################################################################

# Define function to add two numbers
def add_numbers(number_1, number_2):
    sum = number_1 + number_2
    return sum

# Call number addition function
num_1 = float(input('Enter number 1: \n'))
num_2 = float(input('Enter number 2: \n'))
print('Addition: ')
print(add_numbers(num_1, num_2))

# Define function to multiply to numbers
def mul_numbers(number_1, number_2):
    mul = number_1 * number_2
    return mul

# Call number multiplication function
print('Multipication: ')
print(mul_numbers(num_1, num_2))