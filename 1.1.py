########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part I - Python Basics: 1.1
# 
########################################################################


# Numeric data types
print('Numeric data types: \n')
print(type(int(1)))
print(type(float(1.1)))
print(type(complex(1+1j)))
print('\n')

# Sequence data types
print('Sequence data types: \n')
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type(range(1, 10, 1)))
print('\n')

# Text data type
print('Text data type: \n')
print(type(str('Khan')))
print('\n')

# Mapping data type
print('Mapping data type: \n')
print(type({'1': 1, '2':2, '3':3}))
print('\n')

# Set data types
print('Set data types: \n')
print(type({'1','2','3'}))
print(type(frozenset(['1', '2', '3'])))
print('\n')

# Boolean data type
print('Boolean data type: \n')
print(type(True))
print('\n')

# Binary data types
print('Binary data types: \n')
print(type(bytes()))
print(type(bytearray()))
print(type(memoryview(bytearray())))
print('\n')

# None data type
print('None data types: \n')
print(type(None))
print('\n')

# Arithmetic operation in Python for these data types
print('Numeric data types arithmetic operations: \n')
print('Intergers: 1 + 2 = ' + str(int(1)+int(2)))
print('Floating points: 1.1 + 2.1 = ' + str(float(1.1)+float(2.1)))
print('Complex numbers: 1+1j + 2+2j = ' + str(complex(1+1j)+complex(2+2j)))
print('\n')

print('Sequence data type arithmetic operation: \n')
print('Lists: [1, 2, 3] + [3, 2, 1] = ' + str([1, 2, 3]+[3, 2, 1]))
print('\n')

print('Boolean data type arithmetic operation: \n')
print('Boolean: True + True = ' + str(True+True))