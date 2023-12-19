########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part I - Python Basics: 1.3
# 
########################################################################

# Define function to perform operations
def operations(num_1,num_2,operation):
    if operation == '+':
        result = num_1+num_2
    elif operation == '-':
        result = num_1-num_2
    elif operation == '*':
        result =  num_1*num_2
    elif operation == '/':
        result = num_1/num_2
    elif operation =='^':
        result =  num_1**num_2
    else:
        raise ValueError('Invalid operator')
    
    return float(result)

# Choice to continue calculation
cont = True

# Perform calculation
while cont is True:
    number_1 = float(input('Enter first number: '))
    op = input('Enter operator (+,-,*,/,^): ')
    number_2 = float(input('Enter second number: '))
    print(number_1,op,number_2)
    result=operations(number_1,number_2,op)
    print('=',result)
    choise = input('Continue? (y/n): ')
    if choise == 'n':
        cont = False