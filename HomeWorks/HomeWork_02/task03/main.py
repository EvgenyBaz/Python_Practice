# Задайте список из n чисел последовательности $(1+1/n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# сумма 9,06

number = int(input("Введите число: "))
list = {i: round((1+1/i)**i,2) for i in range(1, number+1)}

print(list)

summ = 0
for i in range (1, len(list)+1):
    summ = summ+list[i]

print(summ)

