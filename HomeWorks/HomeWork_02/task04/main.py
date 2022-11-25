# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input("Введите число: "))

list = {i: random.randint(-n, n) for i in range(n)}

print("сприсок чисел", list)

f = open('positions.txt','r')
positions_list = f.readlines()
f.close()

# print("позиции в списке из файла", positions_list)

positions_list = {i: int(positions_list[i].replace("\n","")) for i in range(len(positions_list))}
print("позиции в списке из файла", positions_list)

product = 1
for i in range(len(positions_list)):
    if 0 <= positions_list[i]-1 <= (len(list)-1):
        product = product*list[positions_list[i]-1]
print("произведение", product)