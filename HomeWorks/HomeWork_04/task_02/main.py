# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("введите натуральное число N: "))
multiply = []
i = 1
while number != 1:
    i += 1
    if (number % i) == 0:
        multiply.append(i)
        number = number/i
        i = 1
print(multiply)

