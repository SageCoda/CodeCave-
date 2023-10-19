from sys import builtin_module_names


# color="yellow" 

# if color == 'green':
#     print('Beginner')
# elif color == 'blue':
#     print('Intermediate!')
# elif color == 'red':
#     print('Pro!')
# else:
#     print('No idea whatchu saying')

# # age =input('How old are you?')
# # age =int(age)
    
# # if age >= 21:
# #     print('come in')
# #     print('*******')
# # else:
# #     print('Go home kid!')

# #     print('After the if statement')      


f_name=input('What is your first name? ')
l_name=input('What is your last name? ')

if len(f_name + l_name) < 12:
    print(f"{f_name} {l_name} is shorter than the average American name length by {12-len(f_name + l_name)}")
elif len(f_name + l_name) > 12:
    print(f"{f_name} {l_name} is longer than the average American name length by {len(f_name + l_name)-12}")   
elif len(f_name + l_name) == 12:
     print(f"{f_name} {l_name} is equal to the average American name length") 