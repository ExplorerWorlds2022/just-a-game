def start_game():
    response = input('Желаете начать игру? (Да/Нет) ')
    if response == 'Да':
        while response == 'Да':
            draw_field()
            print('Вводите номер строки и столбца клетки, чтобы поставить туда крестик/нолик')
            response = input('Хотите убить ещё немного времени?')
    elif response == 'Нет':
        print('Мудрое решение!')

def draw_field():
    
    print('''-------
| | | |
-------
| | | |
-------
| | | |
-------''')

def game():
    while check_win() == False:
        x, y = 'Первый игрок ставит крестик'


def check_win():
    pass

print('''Хотите убить немного времени с приятелем? Вы по адресу!
Добро пожаловать в "Крестики Нолики!"''')

start_game()