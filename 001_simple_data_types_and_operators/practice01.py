#task 1

# name = 'Aleksandr'
# surname = 'Gurjev'
# age = 34
# print(f'Hello {name} {surname}.Your age is {age}')

#task 2
# import math
#
# triangle = ('a', 'b', 'c')
# a = 4
# b = 5
# c = math.sqrt(a ** 2 + b ** 2)
# print(c)

#task 3

# triangle = input('a\n''b\n''c\n')
# a, b, c = map(float, input(triangle).split())
# a, b, c = sorted([a, b, c])
#     if a ** 2 + b ** 2 == c ** 2:
#         print('OK')
#     else:
#         print('NOT')

#task 4

# message ='Gimme numbers'
# index = 0
# while index < len(message):
#     index = index + 1
#     print(message[-index])
#task 5

# var_a = 1, 2, 3, 5, 8
# var_b = 8, 2, 5
# var_c = f'{var_a}{var_b}'
#
# print(var_c)

# task 6





# task 7

seconds = 1234565
seconds_in_day = 60 * 60 * 24
seconds_in_hour = 60 * 60
seconds_in_minute = 60

days = seconds // seconds_in_day
hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute

print(days, hours, minutes)



