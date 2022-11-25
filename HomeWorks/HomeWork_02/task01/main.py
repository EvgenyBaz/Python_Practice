# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

number = float(input("введите вещественное число: "))
number = str(number)
number = number.replace("-","")

new_number = number.split(".")

part_a = int(new_number[0])
part_b = int(new_number[1])

summ = 0
while part_a != 0:
    summ = summ + part_a % 10
    part_a = part_a//10
while part_b != 0:
    summ = summ + part_b % 10
    part_b = part_b//10


print(summ)
