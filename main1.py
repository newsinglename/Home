def helo():
    print(" Игра'крестики-нолики' ")
    print(" Форма ввода x, y ")
    print(" x - номер строки ")
    print(" y - номер столбца ")


game_X0 = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def playing_field():
    print(f"  0 1 2")
    print(f"0 {game_X0[0][0]} {game_X0[0][1]} {game_X0[0][2]}")
    print(f"1 {game_X0[1][0]} {game_X0[1][1]} {game_X0[1][2]}")
    print(f"2 {game_X0[2][0]} {game_X0[2][1]} {game_X0[2][2]}")

#coord - вводимые координаты
def coord():
    while True:
        pos = input("         Ваш ход:  ").split()

        if len(pos) != 2:
            print(" Нужно ввести 2 координаты! ")
            continue

        x, y = pos

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Нужно ввести числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2 :
            print(" Нет таких координат! ")
            continue

        if game_X0[x][y] != " " :
            print("Занято!")
            continue

        return x, y

def win():
    win_coord = (((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                 ((0, 2), (1, 1), (2, 0)),((0,0),(1,1),(2,2)),((0,0),(0,1),(2,0)),
                 ((0, 1), (1, 1), (2, 1)),((0,2),(1,2),(2,2)))
    for pos in win_coord:
        simbols = []
        for c in pos:
            simbols.append(game_X0[c[0]][c[1]])

        if simbols == ["X","X","X"]:
            print( " Выиграл X! ")
            return True
        if simbols == ["0","0","0"]:
            print( " Выиграл 0! ")
            return True
    return False



numb = 0
while True:
    numb += 1
    playing_field()
    if numb % 2 == 1:
        print(" Ход крестика ")
    else:
        print(" Ход нолика ")
    x, y = coord()

    if numb % 2 == 1:
        game_X0[x][y] = "X"
    else:
        game_X0[x][y] = "0"

    if win():
        break

    if numb == 9:
        print(" Ничья ")
        break

