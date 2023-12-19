########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part I - Python Basics: 1.5
# 
########################################################################

# Take input from the user
la = input('What programming language do you know?\n')

# Match input to the case statement & provide output
match la:
    case 'Python':
        print('You can develop Andriod applications.')

    case 'PHP':
        print('You can develop backend.')

    case 'Java':
        print('You can develop mobile applications')
        
    case 'JavaScript':
        print('You can develop websites.')
        
    case _:
        print('You should learn Python to solve real world problems.')