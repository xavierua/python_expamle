from random import randint
import os


# Here we choice with size for square you want
side = int(input('Choice which side you want (from 4 to 8)\n'))

# Making a game field, where we use size from variable 'side'
game_field = [['*' for y in range(side)] for x in range(side)]

# Save points
score = 0

# Number when the game ends, if number is 2048 the game will end
is_2048 = 0


def get_index():
    # Get random index for function 'put_number_on_field'
    return randint(0, side-1)


def show_board():
    # Visualising game field
    for x in game_field:
        for y in x:
            print(y, end=' ')
        print()


def check_if_2048(number):
    # Check if someone on board has a 2048 and add to variable
    global is_2048
    is_2048 = number


def create_number():
    # Get number 2 (if random number less than 90) or 4
    return 4 if randint(1, 100) >= 90 else 2


def put_number_on_field():
    # Put number from 'create_number' on game field if the cell is empty
    x = get_index()
    y = get_index()
    if game_field[x][y] != '*':
        put_number_on_field()
    else:
        game_field[x][y] = create_number()


def check_empty_space():
    # Check if there are empty cell ('*') on game field
    for row in game_field:
        for cell in row:
            if cell == '*':
                return True
    return False


def can_move_left_or_right(revers=False):
    # Check if you can move left or right
    for x in range(side):
        if revers:
            game_field[x].reverse()
        for y in range(1, side):
            if game_field[x][y-1] == '*' and game_field[x][y] != '*':
                if revers:
                    game_field[x].reverse()
                return True
            if game_field[x][y-1] == game_field[x][y] and game_field[x][y-1] != '*':
                if revers:
                    game_field[x].reverse()
                return True
        if revers:
            game_field[x].reverse()
    return False


def can_move_up_or_down(revers=False):
    # Check if can move up or down
    if revers:
        game_field.reverse()
    for y in range(side):
        for x in range(1, side):
            if game_field[x-1][y] == '*' and game_field[x][y] != '*':
                if revers:
                    game_field.reverse()
                return True
            if game_field[x-1][y] == game_field[x][y] and game_field[x-1][y] != '*':
                if revers:
                    game_field.reverse()
                return True
    if revers:
        game_field.reverse()
    return False


def your_choice(up, down, left, right):
    # Receive your input and check if you can move, after that show all possible way
    move_list = {
        'up': up,
        'down': down,
        'left': left,
        'right': right
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


def move_up_or_down(revers=False):
    # Move all number on game field up or down
    step = 1
    if revers:
        game_field.reverse()
    for x in range(side):
        for y in range(1, side):
            if game_field[y-1][x] == '*' and game_field[y][x] != '*':
                game_field[y-step][x] = game_field[y][x]
                game_field[y][x] = '*'
                step = 1
            if game_field[y-1][x] == game_field[y][x] and game_field[y][x] == '*':
                step += 1
        step = 1
    if revers:
        game_field.reverse()


def move_left_or_right(revers=False):
    # Move all numbers on game field left or right
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
    global score
    # Addition all numbers (if two number is the same) in rows and addition points to score
    for x in range(side):
        if reverse:
            game_field[x].reverse()
        for y in range(1, side):
            number_one = game_field[x][y-1]
            number_two = game_field[x][y]
            if number_one == number_two and number_one != '*':
                game_field[x][y-1] = number_one + number_two
                game_field[x][y] = '*'
                score += (number_one + number_two)
                if (number_one + number_two) == 2048:
                    check_if_2048(number_one + number_two)
        if reverse:
            game_field[x].reverse()


def addition_column(revers=0):
    global score
    # Addition all numbers (if two numbers is the same) in columns and addition points to score
    if revers:
        game_field.reverse()
    for x in range(side):
        for y in range(1, side):
            number_one = game_field[y-1][x]
            number_two = game_field[y][x]
            if game_field[y-1][x] == game_field[y][x] and game_field[y-1][x] != '*':
                game_field[y-1][x] = number_one + number_two
                game_field[y][x] = '*'
                score += (number_one + number_two)
                if (number_one + number_two) == 2048:
                    check_if_2048(number_one + number_two)
    if revers:
        game_field.reverse()


put_number_on_field()

while is_2048 != 2048:
    put_number_on_field()
    print(f'Your Score - {score}')
    print('=' * 20)
    show_board()
    can_move_up = can_move_up_or_down()
    can_move_down = can_move_up_or_down(True)
    can_move_left = can_move_left_or_right()
    can_move_right = can_move_left_or_right(True)
    choice = input(your_choice(can_move_up, can_move_down, can_move_left, can_move_right))
    while True:
        if check_empty_space() or ((can_move_left or can_move_right) or (can_move_up or can_move_down)):
            if choice == 'a' and can_move_left:
                move_left_or_right()
                addition_row()
                move_left_or_right()
                break
            if choice == 'd' and can_move_right:
                move_left_or_right(True)
                addition_row(True)
                move_left_or_right(True)
                break
            if choice == 'w' and can_move_up:
                move_up_or_down()
                addition_column()
                move_up_or_down()
                break
            if choice == 's' and can_move_down:
                move_up_or_down(True)
                addition_column(True)
                move_up_or_down(True)
                break
        else:
            break
        choice = input()

    if check_empty_space() or ((can_move_left or can_move_right) or (can_move_up or can_move_down)):
        continue
    else:
        print('Game Over')
        break
print(f'Congratulation! You take 2048 and your score is {score}')
