# Создайте программу для игры в ""Крестики-нолики"".


def turn(field, player):

    position = input(f"ход {player[0]} игрока: выберите номер поля: ")

    match position:
        case "1":
            field[0][0] = player[1]
        case "2":
            field[0][1] = player[1]
        case "3":
            field[0][2] = player[1]
        case "4":
            field[1][0] = player[1]
        case "5":
            field[1][1] = player[1]
        case "6":
            field[1][2] = player[1]
        case "7":
            field[2][0] = player[1]
        case "8":
            field[2][1] = player[1]
        case "9":
            field[2][2] = player[1]

    print(*field, sep="\n")
    # проверка выигрыша
    if field[0][0] == field[0][1] == field[0][2]:
        winner = player[0]
    elif field[1][0] == field[1][1] == field[1][2]:
        winner = player[0]
    elif field[2][0] == field[2][1] == field[2][2]:
        winner = player[0]
    elif field[0][0] == field[1][0] == field[2][0]:
        winner = player[0]
    elif field[1][0] == field[1][1] == field[2][1]:
        winner = player[0]
    elif field[2][0] == field[2][1] == field[2][2]:
        winner = player[0]
    elif field[0][0] == field[1][1] == field[2][2]:
        winner = player[0]
    elif field[0][2] == field[1][1] == field[2][0]:
        winner = player[0]
    else:
        winner = "continue"
    return winner

field = []
line = []
player = []


k = 0
for i in range(3):
    line = []
    for j in range(3):
        k += 1
        line.append(str(k))
    field.append(line)

print("игрок 1 : Х , игрок 2 : 0")
print(*field, sep="\n")

player1 = ["1", "X"]
player2 = ["2", "O"]
turn_count = -1
turn_check = "continue"

while turn_check == "continue" and turn_count != 8:
    turn_count +=1
    if turn_count%2 == 0:
        turn_check = turn(field, player1)
    else:
        turn_check = turn(field, player2)

if turn_count !=8:
    print(f"победил игрок {turn_check}")
else:
    print("ничья")