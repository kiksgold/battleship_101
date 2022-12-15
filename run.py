from random import randint

# """
#     -------BATTLESHIPS 101------
#     How it will work:
#     1. A 8x8 grid will have 5 ships of variable length randomly placed about
#     2. You will have 50 bullets to take down the ships that are placed down
#     3. You can choose a row and column such as A3 to indicate where to shoot
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
HIDDEN_GRID = [[''] * 8 for x in range(8)]
# Grid for displaying hits and miss
GUESS_GRID = [[''] * 8 for x in range(8)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


# Define Function to Print Battleship grid size
def print_grid(grid):
    print(' A B C D E F G H')
    print(' ---------------')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# Define Function to create the ships
def create_ships(grid):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while grid[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        grid[ship_row][ship_column] = 'X'


# Define Function to get ship location
def get_ship_location():
    # Enter the row number between 1 to 8
    row = input('Please enter a ship row 1-8: ')
    while row not in '12345678':
        print("Please enter a valid row")
        row = input('Please enter a ship row 1-8: ')

    # Enter the Ship column from A TO H
    column = input('Please enter a ship column A-H: ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column")
        column = input('Please enter a ship column A-H: ').upper()
    return int(row) -1, let_to_num[column]


def count_hit_ships():
    pass




