field = list()


def start_game():
    response = input("Желаете начать игру? (Да/Нет) ")
    if response == "Да":
        print('''Вводите номер строки и столбца клетки, чтобы поставить туда крестик/нолик. 
            Побеждает игрок, поставивший свои символы в одну линию. Приятной игры!''')
        game()
    elif response == "Нет":
        print("Мудрое решение!")
    else:
        print("Некорректный ввод, попробуйте ещё раз!")
        start_game()


def game():
    global field
    line, column = list("-------"), list("| | | |")
    field = [line, column, line, column, line, column, line]
    player_turn = 0
    while check_win() == False:
        draw_field()
        x, y = map(int, input(f"{player_turn + 1} игрок ходит: ").split())
        field[x][y] = "X" if player_turn == 0 else "O"
        player_turn = (player_turn + 1) % 2
    print(f'Победил {p}')


def draw_field():
    for line in field:
        print(*line)


def check_win():
    for line_num in range(1, 7, 2):
        line = field[line_num]
        if line.count("X") == 3:
            return 1
        elif line.count("O") == 3:
            return 2

    for column in range(1, 7, 2):
        if field[1][column] == field[3][column] == field[5][column] == "X":
            return 1
        elif field[1][column] == field[3][column] == field[5][column] == "O":
            return 2
        
    if line[1][1] == line[3][3] == line[5][5] == 'X' or \
    line[1][5] == line[3][3] == line[5][1] == 'X':
        return 1
    elif line[1][1] == line[3][3] == line[5][5] == 'O' or \
    line[1][5] == line[3][3] == line[5][1] == 'O':
        return 2
    
    return False

print(
    '''Хотите убить немного времени с приятелем? Вы по адресу!
Добро пожаловать в "Крестики Нолики!"'''
)
start_game()
