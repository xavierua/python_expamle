from random import randint
from pdb import set_trace


side = int(input('Choise wich side you want (from 4 to 8)\n'))
game_field = [['*' for y in range(side)] for x in range(side)]


def get_index():
    return randint(0, side-1)


def show_board():
    for x in game_field:
        for y in x:
            print(y, end=' ')
        print()


def create_number():
    return 4 if randint(1, 100) >= 90 else 2


def put_number_on_field():
    x = get_index()
    y = get_index()
    if game_field[x][y] != '*':
        put_number_on_field()
    else:
        game_field[x][y] = create_number()


def check_empty_space():
    for row in game_field:
        for cell in row:
            if cell == '*':
                return True
    return False


def can_move_left_or_right(revers=0):
    field = game_field.copy()
    for x in range(side):
        if revers:
            field[x].reverse()
        for y in range(1, side):
            if field[x][y-1] == '*' and field[x][y] != '*':
                return True
            if field[x][y-1] == field[x][y] and field[x][y-1] != '*':
                return True
    return False


def can_move_up_or_down(revers=0):
    field = game_field.copy()
    if revers:
        field.reverse()
    for y in range(side):
        for x in range(1, side):
            if field[x-1][y] == '*' and field[x][y] != '*':
                return True
            if field[x-1][y] == field[x][y] and field[x-1][y] != '*':
                return True
    return False


def your_choice():
    move_list = {
        'up': can_move_up_or_down(),
        'down': can_move_up_or_down(1),
        'left': can_move_left_or_right(),
        'right': can_move_left_or_right(1)
    }
    your_input = ''
    for direction in move_list:
        if move_list[direction]:
            if direction == 'up':
                your_input += 'Press "W" for move up\n'
            if direction == 'down':
                your_input += 'Press "S" for move down\n'
            if direction == 'left':
                your_input += 'Press "A" for move left\n'
            if direction == 'right':
                your_input += 'Press "D" for move right\n'
    return your_input


# def move_up_or_down(revers=0):
#     step = 1
#     if revers:
#         game_field.reverse()
#     for y in range(side):
#         for x in range(1, side):
#             if game_field[x-1][y] == '*' and game_field[x][y] != '*':
#                 game_field[x-step][y] = game_field[x][y]
#                 game_field[x][y] = '*'
#                 step = 1
#             if game_field[x-1][y] == game_field[x][y] and game_field[x-1][y] == '*':
#                 step += 1
#         step = 1
#     if revers:
#         game_field.reverse()


def move_left_or_right(revers=0):
    step = 1
    for x in range(side):
        if revers:
            game_field[x].reverse()
        for y in range(1, side):
            if game_field[x][y-1] == '*' and game_field[x][y] != '*':
                game_field[x][y-step] = game_field[x][y]
                game_field[x][y] = '*'
                step = 1
            if game_field[x][y-1] == game_field[x][y] and game_field[x][y] == '*':
                step += 1
        step = 1
        if revers:
            game_field[x].reverse()


def addition_row(reverse=0):
    for x in range(side):
        if reverse:
            game_field[x].reverse()
        for y in range(1, side):
            number_one = game_field[x][y-1]
            number_two = game_field[x][y]
            if number_one == number_two and number_one != '*':
                game_field[x][y-1] = number_one + number_two
                game_field[x][y] = '*'
        if reverse:
            game_field[x].reverse()


def addition_column(revers=0):
    if revers:
        game_field.reverse()
    for x in range(side):
        for y in range(1, side):
            number_one = game_field[y-1][x]
            number_two = game_field[y][x]
            if number_one == number_two and number_one != '*':
                game_field[y-1][x] = number_one + number_two
                game_field[y][x] = '*'
    if revers:
        game_field.reverse()


while True:
    if check_empty_space():
        put_number_on_field()
    else:
        print('Game Over')
        break
    show_board()
    choice = input(your_choice()).lower()
    while True:
        if choice == 'a':
            move_left_or_right()
            addition_row()
            move_left_or_right()
            break
        if choice == 'd':
            move_left_or_right(1)
            addition_row(1)
            move_left_or_right(1)
            break
        # if choice == 'w':
        #     move_up_or_down()
        #     addition_column()
        #     move_up_or_down()
        #     break
        # if choice == 's':
        #     move_up_or_down(1)
        #     addition_column(1)
        #     move_up_or_down(1)
        #     break
        choice = input()
