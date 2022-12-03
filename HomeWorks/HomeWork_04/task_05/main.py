# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def readpoly(poly):
    poly = poly[:poly.find("=")]
    poly = poly.split("+")
    polynome1 = {}
    for part in poly:
        if part.count('^') == 1:
            power = int(part[part.find('^') + 1:])
            if part.count('*') == 1:
                const = int(part[:part.find('x') - 1])
            else:
                const = 1

        elif part.count('x') == 1:
            power = 1
            if part.count('*') == 1:
                const = int(part[:part.find('x') - 1])
            else:
                const = 1
        else:
            power = 0
            const = int(part)

        polynome1[power] = const

    return polynome1


# ___________________________________


def polynome_gen(dict_n):

    polynome = '=0'

    powers = sorted(dict_n.keys())
    print(powers)

    for pow_d in powers:
        const = dict_n[pow_d]
        if pow_d == 0:
            polynome = "+" + str(const)+polynome
        elif pow_d == 1:
            if const == 1:
                polynome = "+x" + polynome
            else:
                polynome = "+" + str(const) + "*x" + polynome
        else:
            if const == 1:
                polynome = "+x^" + str(pow_d) + polynome
            else:
                polynome = "+" + str(const) + "*x^" + str(pow_d) + polynome

    polynome = polynome[1:]

    return polynome


#    --------------------------------------------
# path_1 = input("введите имя первого файла: ")
# path_2 = input("введите имя второго файла: ")

path_1 = "poly1"
path_2 = "poly3"

file = open(path_1, "r")
poly1 = file.readline()
file.close()

file = open(path_2, "r")
poly2 = file.readline()
file.close()

print(poly1, " ", poly2)

poly_dic1 = readpoly(poly1)
poly_dic2 = readpoly(poly2)

print(poly_dic1, " ", poly_dic2)

sum_dic = {}
for k in poly_dic1.keys():

    sum_dic[k] = poly_dic1[k] + poly_dic2.get(k, 0)
# print(sum_dic)
for k in poly_dic2.keys():
    if poly_dic1.get(k, 0) == 0:
        sum_dic[k] = poly_dic2[k]
print(sum_dic)
# sum_dic = dict(sorted(sum_dic.items(), reverse=True)) ??? не работает??? :(
print(polynome_gen(sum_dic))
