# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


num_list = input("введиите список натуральных чисел через пробел: ")
num_list1 = num_list.split(" ")
unique = []

for check_num in num_list1:

    if num_list.count(check_num) == 1:
        unique.append(check_num)

print(unique)
