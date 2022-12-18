from random import randint

# """
#     -------BATTLESHIPS 101------
#     How it will work:
#     1. A grid size has been set to a minimum of 5 and maximum of 26
#     2> Players can choose the grid size they want to play
#     2> Players can also choose the number of bullets to be shot
#     3. You can choose a row and column such as B5 to indicate where to shoot
#     4. For every shot that hits or misses it will show up in the grid
#     6. If all ships are unearthed before using up all bullets, you win
#         else, you lose and it's game over!

#     Legend:
#     'X' indicates the ships hit
#     '-' indicates the hits missed
#     '' indicates available space
# """

GRID_SIZE_MIN = 5
GRID_SIZE_MAX = 26


def start_game():
    print('Welcome to Battleship 101!!!')

    grid_instruction = 'Please enter grid size between ' + str(GRID_SIZE_MIN) + ' and ' + str(GRID_SIZE_MAX) + ':\n'
    grid_size_set = False
    while grid_size_set is False:
        grid_size = input(grid_instruction)
        try:
            grid_size = int(grid_size)
            if (grid_size >= GRID_SIZE_MIN & grid_size <= GRID_SIZE_MAX):
                grid_size_set = True
            else:
                grid_size = input(grid_instruction)
        except ValueError:
            grid_size = input(grid_instruction)

    MAX_NUM_OF_SHIP = (grid_size * grid_size) - 1
    ship_instruction = 'Please enter number of ship(s) between 1 and ' + str(MAX_NUM_OF_SHIP) + ':\n'
    num_of_ship_set = False
    while num_of_ship_set is False:
        number_of_ships = input(ship_instruction)
        try:
            number_of_ships = int(number_of_ships)
            if (number_of_ships > 0 & number_of_ships <= MAX_NUM_OF_SHIP):
                num_of_ship_set = True
            else:
                number_of_ships = input(ship_instruction)
        except ValueError:
            number_of_ships = input(ship_instruction)

    GRID_SIZE = grid_size
    NUM_OF_SHIPS = number_of_ships

    # Grid for holding ship locations
    HIDDEN_GRID = [[''] * GRID_SIZE for x in range(GRID_SIZE)]
    # Grid for displaying hits and miss
    GUESS_GRID = [[''] * GRID_SIZE for x in range(GRID_SIZE)]

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    LETTERS_LIST = [*LETTERS]

    grid_letters_list = [LETTERS_LIST[i] for i in range(GRID_SIZE)]
    grid_letters = ''.join(grid_letters_list)
    last_grid_letter = grid_letters_list[len(grid_letters_list) - 1]

    # Function to Print Battleship grid size
    def print_grid(grid):
        grid_divider = ['-' for x in range(GRID_SIZE)]
        print(' ' + (' '.join(grid_letters_list)))
        print(' ' + (' '.join(grid_divider)))
        row_num = 1
        for row in grid:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1

    # Function to create the ships
    def create_ships(grid):
        for ship in range(NUM_OF_SHIPS):
            ship_row, ship_column = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
            while grid[ship_row][ship_column] == 'X':
                ship_row, ship_column = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
            grid[ship_row][ship_column] = 'X'

    # Function to get the location to fire
    def get_shoot_location():
        # Enter the row number between 1 to 100
        row_instruction = 'Please enter a ship row 1-' + str(GRID_SIZE) + ':\n '
        rows = map(lambda x: str(x), list(range(1, GRID_SIZE + 1)))
        row = input(row_instruction)
        while row not in rows:
            print("Please enter a valid row")
            row = input(row_instruction)

        # Enter the Ship column from A TO Z
        column_instruction = 'Please enter a ship column A-' + last_grid_letter + ':\n '
        column = input(column_instruction).upper()
        while column not in grid_letters:
            print("Please enter a valid column")
            column = input(column_instruction).upper()
        return int(row) - 1, LETTERS_LIST.index(column)
        print('You have ' + str(turns) + ' turns remaining \n')

    # Function to count hit ships
    def count_hit_ships(board):
        count = 0
        for row in board:
            for column in row:
                if column == 'X':
                    count += 1
        return count

    #  Run all program functions here
    create_ships(HIDDEN_GRID)
    # print_grid(HIDDEN_GRID)

    GAME_TURNS = NUM_OF_SHIPS + 1
    turns = GAME_TURNS
    while turns > 0:
        if turns == GAME_TURNS:
            print('Welcome to Battleship 101!!!')
            print("You have " + str(turns) + " turns to take down " + str(NUM_OF_SHIPS) + " ships \n")
            print("Let's play!\n")
        print_grid(GUESS_GRID)
        row, column = get_shoot_location()
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
        if count_hit_ships(GUESS_GRID) == NUM_OF_SHIPS:
            print_grid(GUESS_GRID)
            print('Congratulations, you have sunk all the battleships')
            break
        print('You have ' + str(turns) + ' turns remaining')
        if turns == 0:
            print('Sorry, you ran out of turns, the game is over')
            break

    start_again = input('Do you want to start again? Enter Y for Yes: \n').upper()
    if start_again == 'Y':
        start_game()


start_game()
