# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list_len = int(input("введите длину списка: "))
list = [random.random()*10 for i in range (list_len)]
list_dec = []

for i in range(list_len):
    list_dec.append(list[i]%1)
print(list)
print(min(list_dec)*max(list_dec))