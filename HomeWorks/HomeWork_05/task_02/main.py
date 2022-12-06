# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

import random

def players_turn(candies, player, bot_brain):
    print(f'{player[0]} игрок')
    if player[0] == "bot":
        if bot_brain:
# тут можно вттавить любую логику
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            if candies > 28:
                candies_taken = 28
            else:
                candies_taken = candies
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        else:
            candies_taken = random.randint(1,(min(candies,28)))
        print(f'{player[0]} игрок взял со стола {candies_taken} конфет')
    else:
        candies_taken = int(input("возмите со стола от 1 до 28 конфет: "))
    return candies_taken

mode = int(input("выберите режим игры: 1 -  два игрока, 2 - игра против бота, 3 - игра против ""умного"" бота: "))
candies = 100
print(f"на столе {candies} конфет ")

if mode == 1:
    player1 = ["1", random.randint(1,2)]
    player2 = ["2", 3-player1[1]]
    bot_brain = False
elif mode == 2:
    player1 = ["1", random.randint(1, 2)]
    player2 = ["bot", 3-player1[1]]
    bot_brain = False
else:
    player1 = ["1", random.randint(1, 2)]
    player2 = ["bot", 3-player1[1]]
    bot_brain = True


if player1[1] > player2[1]:
    first_player = player1
    second_player = player2
else:
    first_player = player2
    second_player = player1

print (f'первым ходит {first_player[0]} игрок \n')

while candies > 0:

    candies = candies - players_turn(candies, first_player, bot_brain)
    print(f"на столе {candies} конфет ")
    if candies == 0:
        print(f'победил {first_player[0]} игрок')
        break

    candies = candies - players_turn(candies, second_player, bot_brain)
    print(f"на столе {candies} конфет ")
    if candies == 0:
        print(f'победил {second_player[0]} игрок')
        break
