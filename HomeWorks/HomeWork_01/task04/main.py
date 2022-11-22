# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("введите номер четверти: "))

match quarter:
    case 1:
        print("x>0, y>0")
    case 2:
        print("x<0, y>0")
    case 3:
        print("x<0, y<0")
    case 4:
        print("x>0, y<0")
    case _:
        print("wrong quarter")
