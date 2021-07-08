# task 1

# import datetime


# birth_date = input('year' ', ' 'month' ', ' 'day: ').split()
#
#
# bday = datetime.date(year=int(birth_date[0]), month=int(birth_date[1]), day=int(birth_date[2]))
# past_bday = datetime.date(year=datetime.date.today().year, month=int(birth_date[1]), day=int(birth_date[2]))
# next_bday = datetime.date(year=datetime.date.today().year + 1, month=int(birth_date[1]), day=int(birth_date[2]))
# today = datetime.date.today()
# if past_bday > today:
#     past_bday = datetime.date(year=datetime.date.today().year - 1, month=int(birth_date[1]), day=int(birth_date[2]))
#     next_bday = datetime.date(year=datetime.date.today().year, month=int(birth_date[1]), day=int(birth_date[2]))
#
#
# print(past_bday - today)
# print(next_bday - today)
# print(birth_date)


# task 2

# import random
#
#
# def Generate_Ticket():
#     numbers = []
#     extra_numbers = []
#     numbers_count = 0
#     extra_numbers_count = 0
#     while numbers_count < 5:
#         number = random.randint(1,47)
#         if number not in numbers:
#             numbers.append(number)
#             numbers_count += 1
#     while extra_numbers_count < 2:
#         number = random.randint(1,5)
#         if number not in extra_numbers or number not in numbers:
#             extra_numbers.append(number)
#             extra_numbers_count += 1
#     print(numbers,extra_numbers)
# for x in range(int(input('How Many Tickets You Want, You poor Bastard? '))):
#     Generate_Ticket()




