
"""
    -------BATTLESHIPS 101------
    How it will work:
    1. A 8x18 grid will have 5 ships of variable length randomly placed about
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

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 8
# Global variable for number of ships to place
num_of_ships = 5
# Global variable for bullets left
bullets_left = 50
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions
ship_positions = [[]]
# Board for holding ship locations
HIDDEN_BOARD = [[''] * 8 for x in range(8)]
# Board for displaying hits and miss
GUESS_BOARD = [[''] * 8 for x in range(8)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
