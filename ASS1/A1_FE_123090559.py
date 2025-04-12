from random import shuffle


def letter_operating():
    """
    Prompt the user to enter letters for left, right, up, and down moves.
    Returns the entered letters.
    """
    while True:
        letter_pure = True
        inputted_string = input("Enter the letters used for left, right, up and down move > ")
        lower_inputted_letters = list(inputted_string.lower())
        # let it be a list to better operated
        inputted_l_spaceless = list()
        for i in lower_inputted_letters:
            if not ord(i) == 32:
                inputted_l_spaceless.append(i)
        # create a new list to reduce spaces but let it valid
        # identify whether it is a small letter
        for i in inputted_l_spaceless:
            if not 97 <= ord(i) <= 122:
                print("please enter letters!")
                letter_pure = False
                break
        if not letter_pure:
            continue
        # check whether there are 4 letters inputted
        if len(inputted_l_spaceless) != 4:
            print("Please enter 4 letters!!")
            continue
        # let it be a set and check whether different
        if len(inputted_l_spaceless) != len(set(inputted_l_spaceless)):
            print("Please enter four different letters!!")
            continue

        l, r, u, d = inputted_l_spaceless
        return l, r, u, d
        break


def structure(list_sol):
    """
    Convert a flat list into a 2D list representing the puzzle structure.
    Returns the 2D list.
    """
    places = []
    row = 0
    x = int(len(list_sol) ** (1 / 2))
    while row <= x - 1:
        places.append([])
        col = 0
        while col <= x - 1:
            places[row].append(list_sol[row * x + col])
            col += 1
        row += 1
    return places


def is_solvable(list_sol):
    """
    Check if the given puzzle configuration is solvable.
    Returns True if solvable, False otherwise.
    """
    sum_inversions = 0
    # for each tile it compares it with the tiles that come before it
    for i in range(len(list_sol)):
        if list_sol[i] == 0:
            pass
        else:
            for j in range(0, i):
                if list_sol[j] > list_sol[i]:
                    sum_inversions += 1
    # if it finds a tile with a lower number
    # it increments the count os inversions
    # for a solvable puzzle the inversions must be even
    if sum_inversions % 2 == 0:
        return True
    else:
        return False


def print_puzzle(places):
    """
    Print the current puzzle layout.
    Returns the row and column indices of the empty space.
    """
    row = 0
    # using a loop to traverse the 2d list
    while row <= 2:
        col = 0
        while col <= 2:
            num = places[row][col]
            print("%-3s" % num, end="")
            # Get the position of " "
            # Checking whether the current tile contains empty space
            if places[row][col] == " ":
                updatingrow = row
                updatingcol = col
            col += 1

        print()
        row += 1
    return updatingrow, updatingcol


def get_right_moves(places, updatingrow, updatingrcol):
    """
    Get the valid moves based on the current position of the empty space.
    Returns a list of valid moves.
    """
    choice = []
    if updatingrow < 2:  # Exist a adjacent tile below " "
        choice.append("up - %s" % u)
    if updatingrow > 0:  # Exist a adjacent tile above " "
        choice.append("down - %s" % d)
    if updatingrcol < 2:  # Exist a adjacent tile right " "
        choice.append("left - %s" % l)
    if updatingrcol > 0:  # Exist a adjacent tile left " "
        choice.append("right - %s" % r)
    return choice


def move(places, updatingrow, updatingcol):
    """
    Perform a move based on user input.
    """
    choice = get_right_moves(places, updatingrow, updatingcol)
    while True:
        try:
            choicestring = ",".join(choice)
            result = input("Enter your move (" + choicestring + ") > ")
            if result == u:
                places[updatingrow + 1][updatingcol], places[updatingrow][updatingcol] \
                    = places[updatingrow][updatingcol], places[updatingrow + 1][updatingcol]
                break
            elif result == l:
                places[updatingrow][updatingcol + 1], places[updatingrow][updatingcol] \
                    = places[updatingrow][updatingcol], places[updatingrow][updatingcol + 1]
                break
            elif (result == r) and (updatingcol - 1 >= 0):
                places[updatingrow][updatingcol - 1], places[updatingrow][updatingcol] \
                    = places[updatingrow][updatingcol], places[updatingrow][updatingcol - 1]
                break
            elif (result == d) and (updatingrow - 1 >= 0):  
                places[updatingrow - 1][updatingcol], places[updatingrow][updatingcol] \
                    = places[updatingrow][updatingcol], places[updatingrow - 1][updatingcol]
                break
            else:
                print("Please follow the instruction to enter!! Please enter only one letter again!")
        except:  # if gamer did not enter the letter
            print("Please follow the instruction to enter!!")


def winning(places, count):
    """
    Check if the puzzle has been solved.
    """
    match = 0
    # check every tile and count matches in total
    for row in range(3):
        for col in range(3):
            if (places[row][col] != row * 3 + (col + 1)) and (places[2][2] != " "):
                return
            elif places[row][col] == row * 3 + (col + 1):
                match += 1
    if places[2][2] == " ":
        match += 1
    if match == 9:
        print("Congratulations! You solved the puzzle in %d moves!" % count)
        return True


def sliding_puzzle():
    """
    function to run the sliding puzzle game.
    """
    print("-" * 80)
    print(" game start!!!")
    print("-" * 80)
    # Create a list include 0~8
    list_sol = [x for x in range(9)]
    while True:

        shuffle(list_sol)
        if is_solvable(list_sol):
            break

    list_sol[list_sol.index(0)] = " "
    places = structure(list_sol)

    updatingrrow, updatingrcol = print_puzzle(places)

    count = 0
    while True:

        move(places, updatingrrow, updatingrcol)
        # Show the layout  after move
        updatingrrow, updatingrcol = print_puzzle(places)
        count += 1

        if winning(places, count):
            break


# Start the game

print("Welcome to Kemeng's sliding puzzle game.")
print("The board has an empty space where an adjacent tile can be slid to.")
print("The objective is to re-arrange the tiles into a sequential order by their numbers.")
print("Left to right, top to bottom, by repeatedly making sliding moves (left, right, up, or down).")
print("-" * 80)
l, r, u, d = letter_operating()
sliding_puzzle()
while True:
    next = input("enter 'n' for another game, or 'q' to end the game > ")
    if next == "n":
        sliding_puzzle()
    elif next == "q":
        print("goodbye!")
        break
    else:
        print("enter again please!")
