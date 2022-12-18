# Battleship 101 Game 


## Introduction
This game is the single-player battleship game, we have made used of grids. Each ship occupies a number of consecutive squares on the grid, arranged either horizontally or vertically. The number of squares for each ship is determined by the type of ship. The ships cannot overlap (i.e., only one ship can occupy any given square in the grid). This grids consists of a minimumof 5 rows and maximum of 26 rows and A-Z columns of the battleship where you can destroy and sink the ships.



## Our main goal
The game is a discovery game which players need to discover their opponents ship positions.

https://battleship-101.herokuapp.com/

![ImageHere](./docs/features/amiresponsive.png)

## How it works
<ul>
<li>
 A grid size has been set to a minimum of 5 and maximum of 26
</li>
<li>
Players can choose the grid size they want to play
</li>
<li>
Players can also choose the number of bullets to be shot
</li>
<li>
You can choose a row and column such as B5 to indicate where to shoot
</li>
<li>
For every shot that hits or misses it will show up in the grid
</li>
<li>
If all ships are unearthed before using up all bullets, you win else, you lose and it's game over!
</li>
</ul>

## Features
<ul>
    <li>Define the pattern grid
    </li>
        <ul>
        <li>we defined a hidden grid of size 10
        </li>
        <li>we defined a guess grid of size 10
        </li>
        <li>we used a letter A-Z and numbers to form the grid
        </li>
        </ul>

![ImageHere](./docs/features/entergridsize.png)

   <li>The Create Ship Function
    </li>
        <ul>
        <li>from random we import randint
        </li>
        <li>we use the for loop function to create the number of our ships
        </li>
        <li>The ship row is the number [1-100]
        </li>
        <li>the ship column is the alphabet [A-Z]
        </li>
        <li>the randint randomly assigns values to the ship row and column
        </li>
        <li>the while loop function continues until the grid row and column is X
        </li>
        <li>The grid will get the values ‘X’ once the hidden pattern and guess pattern hits the same ship
        </li>
        </ul>

![ImageHere](./docs/features/creategrid.png)

<li>Define Print Grid
</li>
    <ul>
    <li>the function print the column grid from A-J
    </li>
    <li>prints the row number ".|" symbol for each row on the grid
    </li>
    </ul>

![ImageHere](./docs/features/creategrid.png)

<li>Function for ship location
</li>
    <ul>
    <li>this validates the row number and column
    </li>
    <li>return the function row less by 1 than the value provided and let_to_num[column]
    </li>
    </ul>

![ImageHere](./docs/features/printgrid.png)

<li>Function for counting ships
</li>
    <ul>
    <li>the count is assigned 0
    </li>
    <li>for each row on the grid and each column in the row if the column ==’X’ the count increases by 1 and returns the count
    </li>
    <li>the function counts the number of ships hit and sunk.
    </li>
    </ul>

![ImageHere](./docs/features/congratulations.png)

<li>The run all function
</li>
    <ul>
    <li>we called the function create_ship that creates the ship
    </li>
    <li>The print_grid (Guess_Pattern) creates the guess_pattern grid.
    </li>
    <li>if the guess_pattern == ‘-‘  then it prints “You have already guessed”.
    </li>
    <li>If the hidden patterns Hidden_Pattern[row][column] == ‘X’: then it prints ‘ Congratulations you have hit the battleship’
    </li>
    <li>If the count_hit_ships and the guess_pattern are exactly same i.e 5 then it will print “Congratulations you have sunk all the battleships” 
    </li>
    <li>Once the turns value becomes zero the program will print “ Game over”.
    </li>
    </ul>

![ImageHere](./docs/features/congratulations.png)
    
</ul>


## Testing
I have manually tested this project by doing the following:
<ul>
<li>I passed the codes through a PEP8 and confirmed there are no errors
</li>
<li>It gives valid input, strings and float numbers are not allowed.
</li>
<li>Tested in my local terminal and the Code Institute Heroku terminal
</li>
</ul>

## Bugs
<ul>
    <li>At the point of deplomyent to Heroku, I could not connet to git connect, i was getting 'internal servive error'. However i was able to deploy through git CLI
    </li>
</ul>

## Validator Testing
<ul>
<li>PEP8
    <ul>
    <li>No errors were returned from pep8online.com
    </li>
    </ul>
</li>
</ul>


## Technology Used
<ul>
    <li>run.py
    </li>
    <li>Heroku
    </li>
</ul>

## Deployment
<ul>
<li> Steps for Deployment
</li>
    <ul>
    <li>Create a new app
    </li>
    <li>Set my config vars to store my sensitive data
    </li>
    <li>Set the buildbacks to Python and NodeJS in that order
    </li>
    <li>Click on deploy
    </li>
    </ul>
</ul>



## Credits
<ul>
<li>walkthrough project
</li>
<li>Sample Readme from Ultimate Battleship
</li>
<li>https://github.com/ArjanCodes/2022-coderoast-battleship/blob/main/after.py
</li>
<li>https://www.tutorialspoint.com/online_python_formatter.htm
</li>
<li>Tutor support
</li>
</ul>