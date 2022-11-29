# # Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# #
# # Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# #
# # Формат входных данных
# # В первой строке подаётся число
# # n
# # n – количество холодильников. В последующих
# # n
# # n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# # 5
# # 5 до
# # 100
# # 100 символов.
# #
# # Формат выходных данных
# # Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
# # Sample Input 1:
# # 6
# # 222anton456
# # a1n1t1o1n1
# # 0000a0000n00t00000o000000n
# # gylfole
# # richard
# # ant0n
# # Sample Output 1:
# # 1 2 3
#
#
#
# def check_infection (frigo_name):
#
#     for i in range(0, len(frigo_name)):
#         if frigo_name[i] == "a":
#             for j in range(i, len(frigo_name)):
#                 if frigo_name[j] == "n":
#                     for k in range(j, len(frigo_name)):
#                         if frigo_name[k] == "t":
#                             for l in range(k, len(frigo_name)):
#                                 if frigo_name[l] == "o":
#                                     for m in range(l, len(frigo_name)):
#                                         if frigo_name[m] == "n":
#                                             return True
#
#     else:
#         return False
# list = ["222anton456", "a1n1t1o1n1", "0000a0000n00t00000o000000n", "gylfole", "richard", "ant0n"]
# for i in range(0, len(list)):
#         print (check_infection(list[i]))
#
#
#
#
#
#
#
#
#
#


n = int(input())
f = []
hacker = ['a', 'n', 't', 'o', 'n', '']
count = 0
otvet = []
for i in range(n):
    u = input()
    f.append(u)
for i in range(len(f)):
    hacker = ['a', 'n', 't', 'o', 'n', '']
    for j in range(len(f[i])):
        if f[i][j] == hacker[0]:
            hacker.pop(0)
        if hacker == ['']:
            count = 1 + i

            otvet.append(count)

            break

print(*otvet)

n = int(input())
list1 = []
for i in range(n):
    a = input()
    if 'a' in a:
        a = a[a.find('a'):]
        if 'n' in a:
            a = a[a.find('n'):]
            if 't' in a:
                a = a[a.find('t'):]
                if 'o' in a:
                    a = a[a.find('o'):]
                    if 'n' in a:
                        list1.append(i + 1)
print(*list1)
