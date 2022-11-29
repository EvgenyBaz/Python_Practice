# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input("введите длину ряда для чисел Фибоначи: "))
if number==0:
    fib_num = [0]
elif number==1:
    fib_num = [1, 0, 1]
else:
    fib_num = [1, 0, 1]
    for i in range(2, number+1):
        temp1 = fib_num[i]+fib_num[i-1]
        fib_num.append(temp1)
    for i in range(2, number+1):
        temp2 = fib_num[1] - fib_num[0]
        fib_num.insert(0,temp2)
print (fib_num)
