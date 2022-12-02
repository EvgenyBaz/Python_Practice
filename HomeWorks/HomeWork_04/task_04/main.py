# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k= int(input("введите степень многочлена: "))
polynome = ''

for i in range(k, 1, -1):
    m = random.randint(0, k)
    if m != 0:
        if m == 1:
            polynome = polynome + "x^" +str(i) + "+"
        else:
            polynome = polynome + str(m) + "*x^" +str(i) + "+"
m = random.randint(0, k)
if m != 0:
    if m == 1:
        polynome = polynome + "x" + "+"
    else:
        polynome = polynome + str(m) + "*x" + "+"

m = random.randint(0, k)
if m != 0:
    polynome = polynome + str(m)

polynome = polynome + '=0'

print(polynome)
file_name = input('введите имя файла для сохранения полинома: ')

file = open(file_name, 'w')
file.write(polynome)
file.close()
