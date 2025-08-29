# 1 - 3
# try:
#     print('Divide two numbers: ')
#     x = input('Enter the first number ')
#     y = input('Enter the first number ')
#     final_num = int(x) / int(y)
# except (ZeroDivisionError, ValueError) as e:
#     print(e)
# else:
#     print(final_num)
# finally:
#     print('End of the program')

# class NegativeNumberError(Exception):
#     def __init__(self, message="Needs to be a positive number"):
#         super().__init__(message)

# num = int(input('Enter a number '))
    
# if not isinstance(num, int):
#     raise ValueError('Input needs to be a number')
# elif int(num) < 0:
#     raise NegativeNumberError
# else:
#     print(f'the value is {num}')

# def inverse(num):
#     result = []
#     for number in num:
#         try:
#             result.append(1 / float(number))
#         except ZeroDivisionError:
#             result.append(float('inf'))
#     return result
    
# print(inverse([1, 2, 0, -5]))

# students = {'John': 25, 'Jane': 22, 'Doe': 30}

# def get_age(name):
#         try:
#             return students[name]
#         except KeyError:
#             return 'Student not found'

# print(get_age('Do'))

numbers = [1, 2, 3, 4, 5]

def fetch_AFNP(lst):
    try:
        return lst[5]
    except IndexError:
        # print('Out of range of Index')
        return None
    
def fetch_LBYL(lst):
    if len(lst) < 6:
        # print('list is too short')
        return None
    else:
        return lst[5]
    
print(fetch_AFNP(numbers))
print(fetch_LBYL(numbers))