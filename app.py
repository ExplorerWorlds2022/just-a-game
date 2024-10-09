field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]    


def game():
    global field

    player_turn, x, y = 0, 0, 0
    for turn in range(9):
        draw_field()
        player_turn = turn % 2 + 1
        print(f"{player_turn} игрок ходите: введите координаты новой клетки")
        while True:
            try:
                x, y = map(int, input().split())
                if check_input():
                    break
            except:       
                print('Неверный формат данных! Введите координаты клетки в формате "2 2"')

        field[x - 1][y - 1] = "X" if player_turn == 1 else "O"
        if check_win():
            break
            
    if check_win():
        print(f'Победил {player_turn} игрок!')
    else:
        print('Ничья!')

    draw_field()


def draw_field():
    for line in field:
        print(f'-------\n|{line[0]}|{line[1]}|{line[2]}|')
        
    print('-------')

def check_win():
    for line in field:
        if line.count("X") == 3 or line.count("O") == 3:
            return True

    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] and field[0][column] != ' ':
            return True
        
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != ' ' or \
    field[0][2] == field[1][1] == field[2][0] and field[0][2] != ' ':
        return True
    
    return False


def check_input(x, y):
    if (1 <= x <= 3 and 1 <= y <= 3) == False:
        print('Такой клетки не существует!')
        return False
    elif field[x-1][y-1] != ' ':
        print('Это поле уже занято!')
        return False
    
    return True


print(
    '''Хотите убить немного времени с приятелем? Вы по адресу!
    Добро пожаловать в "Крестики Нолики!"'''
)

response = input("Желаете начать игру? (Да/Нет) ")
if response == "Да":
    print('''Правила: вводите вначале номер строки, а затем номер столбца клетки, чтобы поставить туда крестик/нолик в формате "2 2". \nПобеждает игрок, поставивший свои символы в одну линию. Приятной игры!''')
    game()
elif response == "Нет":
    print("Мудрое решение!")
else:
    print("Некорректный ввод, попробуйте ещё раз!")