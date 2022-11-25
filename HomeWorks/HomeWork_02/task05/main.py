# Реализуйте алгоритм перемешивания списка.
import random

n = int(input("Введите длину списка: "))
list = {i: i for i in range(n)}

print ("первоначальный список :",list  )

type1 = int(input("выберите тип перемешивания списка : трушный - 0, читерский - 1: "))
if type1 ==0:
    for i in range (len(list)-1):
        position_a = random.randint(0,len(list))
        position_b = random.randint(0,len(list))
        # print(position_a)
        # print(list[position_a])
        # print(position_b)
        # print(list[position_b])

        list[position_a],list[position_b] = list[position_b],list[position_a]

else:
    random.shuffle(list)

print("перемешаный список :",list)