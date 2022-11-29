# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

list_len = int(input("введите длину списка: "))
list = [random.randint(0, 10) for i in range(0, list_len)]
print(list)
multiply_list = []
for i in range (0, list_len//2+list_len%2):
    multiply_list.append(list[i]*list[list_len-i-1])
print(multiply_list)