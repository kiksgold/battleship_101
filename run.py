from random import randint

# """
#     -------BATTLESHIPS 101------
#     How it will work:
#     1. A 10x10 grid will have 5 ships of variable length randomly placed about
#     2. You will have 50 bullets to take down the ships that are placed down
#     3. You can choose a row and column such as B5 to indicate where to shoot
#     4. For every shot that hits or misses it will show up in the grid
#     5. A ship cannot be placed diagonally, so if a shot hits the rest of
#         the ship is in one of 4 directions, left, right, up, and down
#     6. If all ships are unearthed before using up all bullets, you win
#         else, you lose and it's game over!

#     Legend:
#     'X' indicates the ships hit
#     '-' indicates the hits missed
#     '' indicates available space
# """

GRID_SIZE = grid_size
NUM_OF_SHIPS = number_of_ships

# Grid for holding ship locations
HIDDEN_GRID = [[''] * 10 for x in range(10)]
# Grid for displaying hits and miss
GUESS_GRID = [[''] * 10 for x in range(10)]

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS_LIST = [*LETTERS]

grid_letters_list = [LETTERS_LIST[i] for i in range(GRID_SIZE)]
grid_letters = ''.join(grid_letters_list)
last_grid_letter = grid_letters_list[len(grid_letters_list) - 1]


# Function to Print Battleship grid size
def print_grid(grid):
    print(' A B C D E F G H I J')
    print(' -------------------')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# Define Function to create the ships
def create_ships(grid):
    for ship in range(NUM_OF_SHIPS):
        ship_row, ship_column = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
        while grid[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
        grid[ship_row][ship_column] = 'X'


# Function to get the location to fire
def get_shoot_location():
    # Enter the row number between 1 to 
    row_instruction = 'Please enter a ship row 1-' + str(GRID_SIZE) + ':\n '
    rows = map(lambda x: str(x), list(range(1, GRID_SIZE + 1)))
    row = input(row_instruction)
    while row not in row_instruction:
        print("Please enter a valid row")
        row = input(row_instruction)

    # Enter the Ship column from A TO J
    column_instruction = 'Please enter a ship column A-' + last_grid_letter + ':\n '
    column = input(column_instruction).upper()
    column = input('Please enter a ship column A-J:\n ').upper()
    while column not in grid_letters:
        print("Please enter a valid column")
        column = input(column_instruction).upper()
    return int(row) -1, LETTERS_LIST.index(column)
    print('You have ' + str(turns) + ' turns remaining \n')


# Define Function to count hit ships
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


#  Run all our functions here
create_ships(HIDDEN_GRID)
# print_grid(HIDDEN_GRID)
turns = 6
while turns > 0:
    print('Welcome to Battleship 101!!!')
    print('You have 6 turns to take down 5 ships \n')
    print("Let's play!\n")
    print_grid(GUESS_GRID)
    row, column = get_ship_location()
    if GUESS_GRID[row][column] == '-':
        print(' You already guessed that')
    elif HIDDEN_GRID[row][column] == 'X':
        print('Congratulations, you have hit the battleship')
        GUESS_GRID[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, you missed!')
        GUESS_GRID[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_GRID) == 5:
        print('Congratulations, you have sunk all the battleships')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you ran out of turns, the game is over')
        break

