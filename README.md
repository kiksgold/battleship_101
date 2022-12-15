# Battleship 101 Game 

The game is played on four grids, two for each player. The grids are typically square – usually 10×10 – and the individual squares in the grid are identified by letter and number.[10] On one grid the player arranges ships and records the shots by the opponent. On the other grid, the player records their own shots.

Before play begins, each player secretly arranges their ships on their primary grid. Each ship occupies a number of consecutive squares on the grid, arranged either horizontally or vertically. The number of squares for each ship is determined by the type of ship. The ships cannot overlap (i.e., only one ship can occupy any given square in the grid). The types and numbers of ships allowed are the same for each player. These may vary depending on the rules. The ships should be hidden from players sight and it's not allowed to see each other's pieces. The game is a discovery game which players need to discover their opponents ship positions.[11]

## Introduction
This game is the single-player battleship game, we have made used of grids. Each ship occupies a number of consecutive squares on the grid, arranged either horizontally or vertically. The number of squares for each ship is determined by the type of ship. The ships cannot overlap (i.e., only one ship can occupy any given square in the grid). This grids consists of 10 rows and 10 columns of the battleship where you can destroy and sink the ships.

<p>For each event the organizers pre-sell tickets, if they sell out of a particular category, the organizers print more tickets to sell while the unsold ones are thrashed after the event.</p>

## Our main goal
The game is a discovery game which players need to discover their opponents ship positions.

https://battleship-101.herokuapp.com/

![ImageHere](./docs/features/am_iresponsive.png)

## How it works
<ul>
<li>
 A 10x10 grid will have 5 ships randomly placed about
</li>
<li>
You will have 6 turns to take down the ships that are placed down
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
        <li>we used a letter to number dictionary which is the form of key-value pair
        </li>
        <li>update our ticket worksheet
        </li>
        </ul>

![ImageHere](./docs/features/request_ticket.png)

   <li>Calculate the unsold-tickets
    </li>
        <ul>
        <li>compare tickets sold with the inventory inorder to calculate the unsold (if any) for each category
        </li>
        <li>calculate the unsold tickets
        </li>
        <li>updates the unsold worksheet in our spreadsheet
        </li>
        </ul>

![ImageHere](./docs/features/unsold_ticket.png)

<li>Calculate inventory based on averages from the last 3 events
</li>
    <ul>
    <li>calculate the average inventory
    </li>
    <li>the user adds a 20% margin to the calculated averages for future events
    </li>
    <li>updates our inventory worksheet
    </li>
    <li>make recommendations
    </li>
    </ul>

![ImageHere](./docs/features/inventory_ticket.png)
    
</ul>


## Data Model
<p> We imported a spreadsheet from google sheet, where we have our survey data </p>
<p>Our spreadsheet has 3 columns for the different categories of ticket-sales</p>
<p>It contains 10 rows of numbers from past events</p>
<p>It has 3 worksheets for ticket-sales, unsold tickets and future-tickets </p>

![ImageHere](./docs/features/ticket.png)
![ImageHere](./docs/features/unsold.png)
![ImageHere](./docs/features/inventory.png)

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
    <li> I got an error 'No module named gspread'
        <ul>
        <li>I debugged abd discovered my creds.json file was missing
        </li>
        <li>I the reinstalled 'pip3 install gspread google-auth'
        </li>
        </ul>
    </li>
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

![ImageHere](./docs/features/peponline_result.png)

## Technology Used
<ul>
    <li>Gspread
    </li>
    <li>Github
    </li>
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
<li>Love sandwiches walkthrough project
</li>
<li>Sample Readme from Ultimate Battleship
</li>
<li>Tutor support
</li>
</ul>