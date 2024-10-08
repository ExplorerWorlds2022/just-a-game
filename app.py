field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]    


def game():
    global field

    player_turn, x, y = 0, 0, 0
    for turn in range(9):
        draw_field()
        player_turn = turn % 2 + 1
        print(f"{player_turn} игрок ходит:")
        try:
            x, y = map(int, input().split())
        except:       
            while check_input(x, y) == False:
                print('Неверный ввод данных! Введите координаты поля в формате "2 2"')
                x, y = map(int, input().split())

        field[x - 1][y - 1] = "X" if player_turn == 1 else "O"
        if check_win():
            break
            
    if check_win():
        print(f'Победил {player_turn} игрок!')
        draw_field()
    else:
        print('Ничья!')


def draw_field():
    for line in field:
        print(f'-------\n|{line[0]}|{line[1]}|{line[2]}|')
        
    print('-------')

def check_win():
    for line in field:
        if line.count("X") == 3 or line.count("O") == 3:
            return True

    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] == "X" or \
            field[0][column] == field[1][column] == field[2][column] == "O":
            return True
        
    if field[0][0] == field[1][1] == field[2][2] == 'X' or \
    field[0][0] == field[1][1] == field[2][2] == 'X' or \
    field[0][2] == field[1][1] == field[2][0] == 'O' or \
    field[0][2] == field[1][1] == field[2][0] == 'O':
        return True
    
    return False


def check_input(x, y):
    if type(x) == type(y) == int and 1 <= x <= 3 and 1 <= y <= 3 and field[x-1][y-1] == ' ':
        return True
    return False

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