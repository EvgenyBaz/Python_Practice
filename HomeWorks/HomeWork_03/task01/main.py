# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

list_len = int(input("введите длину списка: "))
list = [random.randint(0, 10) for i in range(0, list_len)]
print(list)
summa = 0
for i in range(1, list_len, 2):
    summa = summa + list[i]
print(summa)