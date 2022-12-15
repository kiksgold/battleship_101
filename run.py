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

# Grid for holding ship locations
HIDDEN_GRID = [[''] * 10 for x in range(10)]
# Grid for displaying hits and miss
GUESS_GRID = [[''] * 10 for x in range(10)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}


# Define Function to Print Battleship grid size
def print_grid(grid):
    print(' A B C D E F G H I J')
    print(' -------------------')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# Define Function to create the ships
def create_ships(grid):
    for ship in range(5):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        while grid[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 9), randint(0, 9)
        grid[ship_row][ship_column] = 'X'


# Define Function to get ship location
def get_ship_location():
    # Enter the row number between 1 to 10
    row = input('Please enter a ship row 1-10: ')
    while row not in '12345678':
        print("Please enter a valid row")
        row = input('Please enter a ship row 1-10: ')

    # Enter the Ship column from A TO J
    column = input('Please enter a ship column A-J: ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column")
        column = input('Please enter a ship column A-J: ').upper()
    return int(row) -1, let_to_num[column]


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
    print('Welcome to Battleship 101!!!\n')
    print("Let's play!")
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

