import turtle
import random
from random import randrange, randint

g_time = 0
g_contact = 0

snake_speed = 200
monster_speed = 500
only_count = 0
valid_food_list = [1, 2, 3, 4, 5]
hide_food_list = []
start_time = True
end_time = False
snake_motion = 'Paused'
former_snake_motion = 'Paused'


turtle.tracer(0)
g_screen = turtle.Screen()
g_screen.setup(560, 660)
g_screen.title('Snake')

g_status = turtle.Turtle()
g_status.hideturtle()
g_status.penup()
g_status.goto(-210, 240)

snake_head = turtle.Turtle("square")
snake_head.color('red')
snake_head.left(90)
snake_head.penup()
head_current_location = [12, 12]
head_target_location = []

snake_tail = turtle.Turtle("square")
snake_tail.color('black')
snake_tail.hideturtle()
snake_tail.penup()
snake_tail.pencolor('blue')
snake_tail_length = 0
snake_tail_expand_num = 5
snake_tail_position = []

positions = []
while len(positions) < 8:
    num = random.randint(1, 23)
    if num < 7 or num > 17:
        positions.append(num)

groups = []
while len(groups) < 4:
    group = random.sample(positions, 2)
    if group not in groups:
        groups.append(group)

monster_1 = turtle.Turtle('square')
monster_1.color('purple')
monster_1.penup()
monster_target_location_1 = groups[0]
monster_current_location_1 = monster_target_location_1

monster_2 = turtle.Turtle('square')
monster_2.color('purple')
monster_2.penup()
monster_target_location_2 = groups[1]
monster_current_location_2 = monster_target_location_2

monster_3 = turtle.Turtle('square')
monster_3.color('purple')
monster_3.penup()
monster_target_location_3 = groups[2]
monster_current_location_3 = monster_target_location_3

monster_4 = turtle.Turtle('square')
monster_4.color('purple')
monster_4.penup()
monster_target_location_4 = groups[3]
monster_current_location_4 = monster_target_location_4


def update_status():
    """
    Update the game status displayed on the screen.
    """
    g_status.clear()
    g_status.write('Contact: ' + str(g_contact) + '          Time: ' + str(g_time)
                   + '       Motion: ' + snake_motion, font=('Arial', 16, 'bold'))


def refresh_time():
    """
    Refresh the game time every second after start.
    """
    global g_time
    global start_time
    global end_time

    if start_time:
        start_time = False
        g_screen.ontimer(refresh_time, 1000)
    else:
        if not end_time:
            g_time += 1
            update_status()
            g_screen.ontimer(refresh_time, 1000)
        else:
            return


def display_frame():
    """
    Display the frame of the game board.
    """
    global info

    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(2)
    t.penup()
    t.goto(-250, -290)
    t.pendown()
    for _ in range(3):
        t.fd(500)
        t.left(90)
    t.fd(500)
    t.penup()
    t.goto(-250, 210)
    t.pendown()
    t.left(180)
    t.fd(80)
    t.right(90)
    t.fd(500)
    t.right(90)
    t.fd(80)

    info = turtle.Turtle()
    info.hideturtle()
    info.penup()
    info.goto(-110, 125)
    info.write('Welcome to Snake!\n\nClick anywhere to start, have fun!', font=('Arial', 16, 'normal'))

    update_status()
    g_screen.update()


def show_snake():
    """
    Show the snake on the game board.
    """
    snake_head.goto(-240 + head_current_location[0] * 20, -280 + head_current_location[1] * 20)
    for each_block_location in snake_tail_position:
        snake_tail.goto(-240 + each_block_location[0] * 20, -280 + each_block_location[1] * 20)
        snake_tail.stamp()
    g_screen.update()


def display_food():
    """
    Display the food items on the game board.
    """
    global food_1, food_2, food_3, food_4, food_5

    food_1 = turtle.Turtle()
    food_1.penup()
    food_1.hideturtle()
    food_1.goto(-243 + food_location_1[0] * 20, -290 + food_location_1[1] * 20)
    food_1.write('1', font=('Arial', 15, 'normal'))

    food_2 = turtle.Turtle()
    food_2.penup()
    food_2.hideturtle()
    food_2.goto(-243 + food_location_2[0] * 20, -290 + food_location_2[1] * 20)
    food_2.write('2', font=('Arial', 15, 'normal'))

    food_3 = turtle.Turtle()
    food_3.penup()
    food_3.hideturtle()
    food_3.goto(-243 + food_location_3[0] * 20, -290 + food_location_3[1] * 20)
    food_3.write('3', font=('Arial', 15, 'normal'))

    food_4 = turtle.Turtle()
    food_4.penup()
    food_4.hideturtle()
    food_4.goto(-243 + food_location_4[0] * 20, -290 + food_location_4[1] * 20)
    food_4.write('4', font=('Arial', 15, 'normal'))

    food_5 = turtle.Turtle()
    food_5.penup()
    food_5.hideturtle()
    food_5.goto(-243 + food_location_5[0] * 20, -290 + food_location_5[1] * 20)
    food_5.write('5', font=('Arial', 15, 'normal'))


def display_monster():
    """
    Display the monsters on the game board.
    """
    monster_list = [monster_1, monster_2, monster_3, monster_4]
    for i, monster in enumerate(monster_list, start=1):
        monster.goto(-230 + globals()[f"monster_target_location_{i}"][0] * 20,
                     -270 + globals()[f"monster_target_location_{i}"][1] * 20)
    g_screen.update()


def display_over():
    """
    Display the game over message on the screen.
    """
    over = turtle.Turtle()
    over.penup()
    over.hideturtle()
    over.pencolor('red')
    over.goto(-110, 0)
    over.write('Game Over!!', font=('Arial', 25, 'bold'))


def display_win():
    """
    Display the game win message on the screen.
    """
    win = turtle.Turtle()
    win.penup()
    win.hideturtle()
    win.pencolor('red')
    win.goto(-110, 0)
    win.write('Winner!!', font=('Arial', 25, 'bold'))

def is_food_valid(loc_1, loc_2, loc_3, loc_4, loc_5):
    """
    Check if the food items are valid.
    """
    loc_list = list(set([(loc_1[0], loc_1[1]), (loc_2[0], loc_2[1]),
                         (loc_3[0], loc_3[1]), (loc_4[0], loc_4[1]),
                         (loc_5[0], loc_5[1])]))
    return len(loc_list) == 5 and (12, 12) not in loc_list


def show_food():
    """
    Show the food items on the game board.
    """
    global food_location_1, food_location_2, food_location_3, food_location_4, food_location_5
    global original_food_pos_1, original_food_pos_2, original_food_pos_3, original_food_pos_4, original_food_pos_5

    food_location_1 = [randrange(0, 25), randrange(0, 25)]
    food_location_2 = [randrange(0, 25), randrange(0, 25)]
    food_location_3 = [randrange(0, 25), randrange(0, 25)]
    food_location_4 = [randrange(0, 25), randrange(0, 25)]
    food_location_5 = [randrange(0, 25), randrange(0, 25)]

    original_food_pos_1 = food_location_1[:]
    original_food_pos_2 = food_location_2[:]
    original_food_pos_3 = food_location_3[:]
    original_food_pos_4 = food_location_4[:]
    original_food_pos_5 = food_location_5[:]

    if not is_food_valid(food_location_1, food_location_2,
                         food_location_3, food_location_4, food_location_5):
        show_food()


def up():
    """
    Set the snake motion for up.
    """
    global snake_motion
    snake_motion = 'Up'


def down():
    """
    Set the snake motion for down.
    """
    global snake_motion
    snake_motion = 'Down'


def left():
    """
    Set the snake motion for left.
    """
    global snake_motion
    snake_motion = 'Left'


def right():
    """
    Set the snake motion for right.
    """
    global snake_motion
    snake_motion = 'Right'


def paused():
    """
    Set the snake motion for paused.
    """
    global snake_motion
    global former_snake_motion

    if snake_motion != 'Paused':
        former_snake_motion = snake_motion
        snake_motion = 'Paused'
    else:
        snake_motion = former_snake_motion


def movable(loc):
    """
    Check whether the location is movable.
    """
    return 0 <= loc[0] <= 24 and 0 <= loc[1] <= 24


def snake_move():
    """
    Set the snake movement.
    """
    global snake_motion
    global snake_speed
    global head_target_location
    global head_current_location
    global snake_tail_length
    global snake_tail_position
    tail_to_expand_position = [12, 12]

    if game_over():
        return
    else:
        if snake_motion != 'Paused':
            if snake_motion == 'Up':
                update_status()
                head_target_location = [head_current_location[0], head_current_location[1] + 1]
            elif snake_motion == 'Down':
                update_status()
                head_target_location = [head_current_location[0], head_current_location[1] - 1]
            elif snake_motion == 'Left':
                update_status()
                head_target_location = [head_current_location[0] - 1, head_current_location[1]]
            elif snake_motion == 'Right':
                update_status()
                head_target_location = [head_current_location[0] + 1, head_current_location[1]]

            if movable(head_target_location):
                if snake_tail_length > 0:
                    tail_to_expand_position = snake_tail_position[snake_tail_length - 1]
                    for i in range(snake_tail_length):
                        if i <= snake_tail_length - 1:
                            snake_tail_position[snake_tail_length - i - 1] \
                                = snake_tail_position[snake_tail_length - i - 2]
                    snake_tail_position[0] = head_current_location
                head_current_location = head_target_location

                if snake_tail_expand_num != 0:
                    snake_expand(tail_to_expand_position)
                else:
                    snake_speed = 200
                snake_tail.clearstamps()
                eat_food()
                show_snake()
                g_screen.ontimer(snake_move, snake_speed)
            else:
                g_screen.ontimer(snake_move, snake_speed)
        else:
            update_status()
            g_screen.ontimer(snake_move, snake_speed)


def snake_expand(pos):
    """
    Expand the snake.
    """
    global snake_tail_length
    global snake_tail_expand_num
    global snake_tail_position
    global snake_speed

    snake_speed = 400
    snake_tail_position.append(pos)
    snake_tail_length += 1
    snake_tail_expand_num -= 1


def is_monster_movable(loc):
    """
    Check whether the monster is movable.
    """
    return 0 <= loc[0] <= 23 and 0 <= loc[1] <= 23


def set_monster_speed():
    """
    Set the monster speed randomly.
    """
    global monster_speed_1, monster_speed_2, monster_speed_3, monster_speed_4
    monster_speed_1 = randrange(monster_speed-50, monster_speed+100, 5)
    monster_speed_2 = randrange(monster_speed-50, monster_speed+100, 7)
    monster_speed_3 = randrange(monster_speed-50, monster_speed+100, 8)
    monster_speed_4 = randrange(monster_speed-50, monster_speed+100, 6)
    g_screen.ontimer(set_monster_speed, 3000)


def monster_move_1():
    """
    Set the monster1 movement.
    """
    global monster_speed_1
    global monster_current_location_1
    global monster_target_location_1

    if game_over():
        return
    else:
        d_x, d_y = head_current_location[0] - monster_current_location_1[0], head_current_location[1] - \
                   monster_current_location_1[1]
        if d_y >= d_x and d_y >= -d_x and d_y >= 0:
            monster_target_location_1 = [monster_current_location_1[0], monster_current_location_1[1] + 1]
        elif -d_x <= d_y <= d_x and d_x >= 0:
            monster_target_location_1 = [monster_current_location_1[0] + 1, monster_current_location_1[1]]
        elif d_y <= d_x and d_y <= -d_x and d_y <= 0:
            monster_target_location_1 = [monster_current_location_1[0], monster_current_location_1[1] - 1]
        elif d_x <= d_y <= -d_x and d_x <= 0:
            monster_target_location_1 = [monster_current_location_1[0] - 1, monster_current_location_1[1]]

        if is_monster_movable(monster_target_location_1):
            monster_current_location_1 = monster_target_location_1
            count_contact()
            display_monster()
            g_screen.ontimer(monster_move_1, monster_speed_1)
        else:
            monster_target_location_1 = monster_current_location_1
            count_contact()
            g_screen.ontimer(monster_move_1, monster_speed_1)


def monster_move_2():
    """
    Set the monster2 movement.
    """
    global monster_speed_2
    global monster_current_location_2
    global monster_target_location_2

    if game_over():
        return
    else:
        d_x = head_current_location[0] - monster_current_location_2[0]
        d_y = head_current_location[1] - monster_current_location_2[1]
        if d_y >= d_x and d_y >= -d_x and d_y >= 0:
            monster_target_location_2 = [monster_current_location_2[0], monster_current_location_2[1] + 1]
        elif -d_x <= d_y <= d_x and d_x >= 0:
            monster_target_location_2 = [monster_current_location_2[0] + 1, monster_current_location_2[1]]
        elif d_y <= d_x and d_y <= -d_x and d_y <= 0:
            monster_target_location_2 = [monster_current_location_2[0], monster_current_location_2[1] - 1]
        elif d_x <= d_y <= -d_x and d_x <= 0:
            monster_target_location_2 = [monster_current_location_2[0] - 1, monster_current_location_2[1]]

        if is_monster_movable(monster_target_location_2):
            monster_current_location_2 = monster_target_location_2
            count_contact()
            display_monster()
            g_screen.ontimer(monster_move_2, monster_speed_2)
        else:
            monster_target_location_2 = monster_current_location_2
            count_contact()
            g_screen.ontimer(monster_move_2, monster_speed_2)


def monster_move_3():
    """
    Set the monster3 movement.
    """
    global monster_speed_3
    global monster_current_location_3
    global monster_target_location_3

    if game_over():
        return
    else:
        d_x = head_current_location[0] - monster_current_location_3[0]
        d_y = head_current_location[1] - monster_current_location_3[1]
        if d_y >= d_x and d_y >= -d_x and d_y >= 0:
            monster_target_location_3 = [monster_current_location_3[0], monster_current_location_3[1] + 1]
        elif -d_x <= d_y <= d_x and d_x >= 0:
            monster_target_location_3 = [monster_current_location_3[0] + 1, monster_current_location_3[1]]
        elif d_y <= d_x and d_y <= -d_x and d_y <= 0:
            monster_target_location_3 = [monster_current_location_3[0], monster_current_location_3[1] - 1]
        elif d_x <= d_y <= -d_x and d_x <= 0:
            monster_target_location_3 = [monster_current_location_3[0] - 1, monster_current_location_3[1]]

        if is_monster_movable(monster_target_location_3):
            monster_current_location_3 = monster_target_location_3
            count_contact()
            display_monster()
            g_screen.ontimer(monster_move_3, monster_speed_3)
        else:
            monster_target_location_3 = monster_current_location_3
            count_contact()
            g_screen.ontimer(monster_move_3, monster_speed_3)


def monster_move_4():
    """
    Set the monster4 movement.
    """
    global monster_speed_4
    global monster_current_location_4
    global monster_target_location_4

    if game_over():
        return
    else:
        d_x = head_current_location[0] - monster_current_location_4[0]
        d_y = head_current_location[1] - monster_current_location_4[1]
        if d_y >= d_x and d_y >= -d_x and d_y >= 0:
            monster_target_location_4 = [monster_current_location_4[0], monster_current_location_4[1] + 1]
        elif -d_x <= d_y <= d_x and d_x >= 0:
            monster_target_location_4 = [monster_current_location_4[0] + 1, monster_current_location_4[1]]
        elif d_y <= d_x and d_y <= -d_x and d_y <= 0:
            monster_target_location_4 = [monster_current_location_4[0], monster_current_location_4[1] - 1]
        elif d_x <= d_y <= -d_x and d_x <= 0:
            monster_target_location_4 = [monster_current_location_4[0] - 1, monster_current_location_4[1]]

        if is_monster_movable(monster_target_location_4):
            monster_current_location_4 = monster_target_location_4
            count_contact()
            display_monster()
            g_screen.ontimer(monster_move_4, monster_speed_4)
        else:
            monster_target_location_4 = monster_current_location_4
            count_contact()
            g_screen.ontimer(monster_move_4, monster_speed_4)


def eat_food():
    """
    Set the snake eating the foods.
    """
    global snake_tail_expand_num

    for i in range(1, 6):
        food_location = globals()[f"food_location_{i}"]
        if food_location == head_current_location:
            globals()[f"food_{i}"].clear()
            food_location[0] = -1
            food_location[1] = -1
            valid_food_list.remove(i)
            snake_tail_expand_num += i


def hide_food():
    """
    Set the food changing position.
    """
    global valid_food_list, hide_food_list, only_count

    def hide_food_func(food_num):
        global original_food_pos_1, original_food_pos_2, original_food_pos_3, original_food_pos_4, original_food_pos_5
        global food_location_1, food_location_2, food_location_3, food_location_4, food_location_5
        food_location = globals().get(f'food_location_{food_num}')
        original_food_pos = globals().get(f'original_food_pos_{food_num}')
        food = globals().get(f'food_{food_num}')
        original_food_pos[0] = food_location[0]
        original_food_pos[1] = food_location[1]
        food.clear()
        food_location[0] = -1
        food_location[1] = -1

    def show_food_func(food_num, number):
        global original_food_pos_1, original_food_pos_2, original_food_pos_3, original_food_pos_4, original_food_pos_5
        global food_location_1, food_location_2, food_location_3, food_location_4, food_location_5
        food_location = globals().get(f'food_location_{food_num}')
        original_food_pos = globals().get(f'original_food_pos_{food_num}')
        food = globals().get(f'food_{food_num}')
        food_location[0] = original_food_pos[0]
        food_location[1] = original_food_pos[1]
        food.goto(-243 + food_location[0] * 20, -290 + food_location[1] * 20)
        food.write(str(number), font=('Arial', 15, 'normal'))

    if not end_time:
        former_hide_food_list = hide_food_list
        hide_food_list = []

        valid_food_length = len(valid_food_list)
        if valid_food_length != 1 and valid_food_length != 0:
            hide_num = 1
        elif valid_food_length == 1 and only_count < 1:
            only_count += 1
            hide_num = randint(0, 1)
        else:
            hide_num = 0
        if start_time:
            hide_num = 0
        hide_food_list = random.sample(valid_food_list, hide_num)

        for i in range(1, 6):
            if i in former_hide_food_list and i not in hide_food_list:
                show_food_func(i, i)
            elif i in hide_food_list and i not in former_hide_food_list:
                hide_food_func(i)

        g_screen.ontimer(hide_food, 5000)


def game_over():
    """
    Set the game over status.
    """
    global end_time
    for monster_location in [monster_current_location_1, monster_current_location_2, monster_current_location_3,
                             monster_current_location_4]:
        if -1 <= monster_location[0] - head_current_location[0] <= 0 and -1 <= monster_location[1] - \
                head_current_location[1] <= 0:
            display_over()
            end_time = True
            return True

    if snake_tail_length == 20:
        display_win()
        end_time = True
        return True

    return False


def count_contact():
    """
    Count the contacts of snake and monster.
    """
    global g_contact
    for each_block in snake_tail_position:
        if -1 <= monster_current_location_1[0] - each_block[0] <= 0 and \
                -1 <= monster_current_location_1[1] - each_block[1] <= 0:
            g_contact += 1
        elif -1 <= monster_current_location_2[0] - each_block[0] <= 0 and \
                -1 <= monster_current_location_1[1] - each_block[1] <= 0:
            g_contact += 1
        elif -1 <= monster_current_location_3[0] - each_block[0] <= 0 and \
                    -1 <= monster_current_location_3[1] - each_block[1] <= 0:
            g_contact += 1
        elif -1 <= monster_current_location_4[0] - each_block[0] <= 0 and \
                    -1 <= monster_current_location_3[1] - each_block[1] <= 0:
            g_contact += 1
            update_status()
            return


def start_game(x, y):
    """
    Set the game start status.
    """
    global info
    global g_time
    info.clear()
    g_screen.onclick(None)
    display_food()
    hide_food()
    refresh_time()
    snake_move()
    set_monster_speed()
    monster_move_1()
    monster_move_2()
    monster_move_3()
    monster_move_4()
    return x, y


def main():
    """
    Set the main function.
    """
    display_frame()
    show_snake()
    display_monster()
    show_food()
    g_screen.onkey(up, 'Up')
    g_screen.onkey(down, 'Down')
    g_screen.onkey(left, 'Left')
    g_screen.onkey(right, 'Right')
    g_screen.onkey(paused, 'space')
    g_screen.onclick(start_game)
    g_screen.listen()
    g_screen.mainloop()

if __name__ == '__main__':
    main()

