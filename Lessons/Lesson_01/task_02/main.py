# 1.
# Напишите программу, которая будет на вход принимать число N и выводить числа от - N до N
#
# *Примеры: *
#
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 2.
# Напишите программу, которая будет принимать на вход дробь и показывать первую
# цифру дробной части числа.
# *Примеры: *
#
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
# 3.
# Напишите программу, которая принимает на вход число и проверяет, кратно
# ли оно 5 и 10 или 15, но не 30.


# n=int(input("введите число N"))
#
# for i in range (-n, n+1):
#     print(i, end=" ")

# n=float(input("введите число n  "))
#
# n=abs(n)
# n = (n - n // 1)
#
# if n==0:
#     print("нет")
# else:
#     n=n*10
#     n = n // 1
#     print(int(n))

n=int(input("введите число N"))

if ((n%5==0) and (n%10==0)) or (n%15==0):
    if (n%30!=0):
        print("да")
    else:
        print("нет")
else:
    print("нет")