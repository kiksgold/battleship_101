
"""
    -------BATTLESHIPS 101------
    How it will work:
    1. A 8x8 grid will have 5 ships of variable length randomly placed about
    2. You will have 50 bullets to take down the ships that are placed down
    3. You can choose a row and column such as A3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A ship cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down
    6. If all ships are unearthed before using up all bullets, you win
        else, you lose and it's game over!

    Legend:
    'X' indicates the ships hit
    '-' indicates the hits missed
    '' indicates available space
"""

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

def create_ships():
    pass

def get_ship_location():
    pass

def count_hit_ships():
    pass




