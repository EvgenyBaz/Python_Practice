# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

#
# input_str = input("ввдите строку: ")
#
# res = (lambda x: 'plr' in x)(input_str)
#
# print (res)
#
print((lambda x: 'plr' in x)(input()))
#
#
# a = int(input('Введите а: '))
# b = int(input('Введите в: '))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
#
# print(a)
# import random
# a = random.randint(33, 99)
# b = random.randint(33, 99)
# c = [a, b]
# print(c)
# while max(a, b) % min(a, b) != 0:
#     if a > b:
#         a = a % b
#     elif a < b:
#         b = b % a
# print(min(a, b))

