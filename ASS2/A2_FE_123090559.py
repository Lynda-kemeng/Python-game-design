import turtle
import random


block_size = 100
game_size = 3
matrix = []

def get_game_size():
    """
    Get the size of the game.
    """
    while True:
        game_size = int(
        turtle.numinput("Sliding Puzzle", "Enter the size of the game (3, 4, or 5): ", minval=3, maxval=5))
        if game_size in [3, 4, 5]:
            return game_size
        else:
            print("Invalid input. Please enter a valid size (3,4 or 5). ")

def generate_matrix(size):
    """
    Generate the game marix.
    """
    while True:
        nums = random.sample(range(size*size), size*size)
        if  is_solvable(nums):
            break
    result=[]
    for i in range(0,len(nums),size):
        result.append(nums[i:i+size])
    return result

def count_inversions(sequence):
    """
    Calculate the number of inversions in the sequence.
    """
    list_num = []
    for i in sequence:
        list_num.append(i)
    b=list_num.index(0)
    list_num.remove(0)
    sum_inversions = 0
    for i in range(len(list_num)):
        for j in range(0, i):
            if list_num[j] > list_num[i]:
                sum_inversions += 1
    return sum_inversions,b


def is_solvable(sequence):
    """
    Check if the game is solvable based on the number of inversions.
    """
    sum_inversions,b= count_inversions(sequence)
    if len(sequence) in [9,25]:
        return sum_inversions % 2 == 0
    if len(sequence) == 16:
        if (b // 4 + 1) in [1, 3]:
            return sum_inversions % 2 == 1
        elif (b // 4 + 1) in [2, 4]:
            return sum_inversions % 2 == 0
        else:
            return False

def create_block(x, y, number, color):
    """
    Create a block for the sliding puzzle.
    """
    t = turtle.Turtle("square")
    t.up()
    t.shapesize(4.5,4.5,1)
    t.goto(x + 50, y - 50)
    t.color(color)

    t.stamp()

    if number != 0:
        t.up()
        t.color("black")
        t.goto(x + 50, y - 70)
        t.write(number, align="center", font=("Arial", 20, "normal"))
        t.down()
    t.hideturtle()

    return t

def display_puzzle():
    """
    Display the sliding puzzle game.
    """
    turtle.clear()
    turtle.speed(0)
    turtle.tracer(0, 0)
    x = -game_size * 100 // 2
    y = game_size * 100 // 2
    for i in range(game_size):
        for j in range(game_size):
            if check_win():
                color = "red" if matrix[i][j] != 0 else 'white'
            else:
                color = "green" if matrix[i][j] != 0 else 'white'
            draw_block(x + j * 100, y - i * 100, matrix[i][j],color)
    turtle.hideturtle()

def display_puzzle_without(m,n):
    """
    Display the sliding puzzle game, without displaying tile at m,n.
    """
    turtle.clear()
    turtle.speed(0)
    turtle.tracer(0, 0)
    x = -game_size * 100 // 2
    y = game_size * 100 // 2
    for i in range(game_size) :
        for j in range(game_size):
            if i != m or j != n:
                if check_win():
                    color = "red" if matrix[i][j] != 0 else 'white'
                else:
                    color = "green" if matrix[i][j] != 0 else 'white'
                draw_block(x + j * 100, y - i * 100, matrix[i][j],color)
    turtle.hideturtle()

def draw_block(x, y, num,color):
    """
    Draw a block for the sliding puzzle.
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.pencolor('white')
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(block_size)
        turtle.right(90)
    turtle.end_fill()
    turtle.pencolor('black')


    if num != 0:
        turtle.up()
        turtle.goto(x + 100 // 2, y - 100 // 2)
        turtle.down()
        turtle.write(num, align="center", font=("Arial", 20, "normal"))


def move(row=None, col=None, row_next=None, col_next=None, status=False):
    if status:
        x = -game_size * 100 // 2
        y = game_size * 100 // 2
        x_next = x + col_next * 100
        y_next = y - row_next * 100
        current_x, current_y = x + col * 100, y - row * 100

        for i in range(game_size):
            for j in range(game_size):
                if (i, j) != (row, col) and (i, j) != (row_next, col_next):
                    draw_block(-game_size * 100 // 2 + j * 100, game_size * 100 // 2 - i * 100, matrix[i][j],"green")

        def animate_move():
            nonlocal current_x, current_y
            if abs(current_x - x_next) > 0.1 or abs(current_y - y_next) > 0.1:
                current_y = (row - row_next) * 0.05 * 100 + current_y
                current_x = -(col - col_next) * 0.05 * 100 + current_x
                turtle.clear()
                display_puzzle_without(row_next,col_next)
                draw_block(current_x, current_y, matrix[row][col],"green")
                turtle.update()
                turtle.ontimer(animate_move, 2)
            else:
                turtle.clear()
                display_puzzle()

        animate_move()
    else:
        display_puzzle()
    if check_win():
        game_solved = True
        turtle.textinput("恭喜！","您已经成功解决了拼图！")

def check_move(row,col):
    """
    Check if a block can be moved in the sliding puzzle.
    """
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in moves:
        if  0 <= row + dy < game_size and 0 <= col + dx < game_size :
            if matrix[row][col] != 0 and matrix[row + dy][col + dx] == 0:
                return True
    return False

def get_index(matrix,element):
    """
    Get the row and column indices of an element in the matrix.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==element:
                return i,j
    return None

clicked_num = None

def click_operating(x,y):
    """
    Operate the click of tile to handle the movement of blocks in the sliding puzzle.
    """
    global matrix, clicked_num
    row = int((-y + game_size / 2 * 100) // 100)
    col = int((x + game_size / 2 * 100) // 100)
    index = col*game_size + row

    if index >= 0 and index < game_size**2:
        clicked_num = row,col
        clicked_row, clicked_col = clicked_num
    else:
        return
    if check_move(clicked_row, clicked_col) == True:
        tar_row, tar_col = get_index(matrix, 0)
        matrix[tar_row][tar_col] = matrix[clicked_row][clicked_col]
        matrix[clicked_row][clicked_col] = 0
        move(clicked_row, clicked_col, tar_row, tar_col, status = True)
        check_win()
        clicked_num = None
        return
    else:
        clicked_num = row, col
        return

def check_win():
    """
    Check if the sliding puzzle is solved.
    """
    sequence = list(range(1, game_size * game_size)) + [0]
    if sum(matrix, []) == sequence:
        return True
    else :
      return False

def main():
    """
    Main function to start the sliding puzzle game.
    """
    global game_size, matrix,game_solved
    game_solved = False
    game_size=get_game_size()
    matrix = generate_matrix(game_size)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.title("Sliding Puzzle Game")
    turtle.setup(800, 800)
    move(status=False)
    turtle.onscreenclick(click_operating)
    turtle.mainloop()

if __name__ == "__main__":
    main()
