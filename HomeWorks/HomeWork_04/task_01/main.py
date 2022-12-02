# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

tolerance = float(input("Задайте точность определения числа в виде десятичной дроби, например 0.001: "))
number = float(input("введите вещественное число: "))

tolerance = len(str(tolerance))-str(tolerance).find(".")-1

print(tolerance)
print(round(number, tolerance))