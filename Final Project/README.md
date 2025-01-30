# SUPER TIC TAC TOE
### Video Demo: https://www.youtube.com/watch?v=84pPJRnaXDI
### Description:
This is a(nother) Tic Tac Toe game made with Python, but it includes some additional features. It runs on the web using Flask, asks for the name of each player, and also allows players to choose different marks to play with. The main difference is that players can choose from different board grid sizes. This game includes 4x4 and 5x5 grids, in addition to the classic and default 3x3 grid. This doesn't necessarily make the game more fun, but it adds a new level of challenge to the coding process.

### Why?
I thought a lot about the project and tried different things. But then I realized that I wanted to learn something useful for my aspirations, so I decided to focus on some frontend work as well. I started learning how to use Flask and did some research on HTML and CSS. And this is the result.

### Requirements
The only external package needed is Flask.

### Files

#### project.py:
This is the server for the game.
Each cell of the board has a dynamically assigned coordinate (row, column).</br>
There are three global dictionaries managing the data for the players:</br>
The first one is an ordereddict, that links the player's name to a list. This list stores tuples, each representing a coordinate pointing to the cell the player has played on the board.</br>
The second dictionary links the player's name to a number that counts how many times that player has won the game.</br>
The third dictionary links the player's name to the selected mark, with each mark being a PNG image.

The game goes like this:</br>
First, home() is called. There, the players choose their names and marks to play. The first thing the function does is clear all variables from any previous values. Then, it stores the values given by the players or assigns default names and marks if none were provided.</br>
When players click START, game() is called. This function checks if a player has reached the maximum of 99 wins. If someone has, it redirects to home() again; if not, it redirects to player1().</br>
player1() reads the name of the first player and passes it to the function playTurn().</br>
playTurn() reads the list of coordinates from the player passed in the arguments, then checks if there is a winner. If not, it checks which cell the player clicks on and immediately assigns the cell's coordinates to the player's coordinates list. Then it redirects to player2(), and everything goes the same for the second player in the players dictionary.</br>
If there is a winner, it adds 1 to the player's win count and redirects to winner_is(). This function simply shows the name of the winner, disables all remaining cells on the board, and checks for the HOME or PLAY AGAIN buttons.

The winner() function is the heart of the game. It works regardless of how many cells the board has. The project sets a fixed size that players can choose to avoid cluttering the screen with an oversized board. However, this function could determine a winner even with a 1000x1000 grid. </br>
A player needs to control a column, a row, or a diagonal to win.</br>
In the board’s coordinate system, a column means the player has the same number of coordinates with a constant value in y as the board's size on the y axis.</br>
Similarly, a row means the player has the same number of coordinates with a constant value in x as the board's size on the x axis.</br>
The diagonal from the upper left to the bottom right consists of all coordinates that are matching pairs, with the same value in x and y for the size of the board.</br>
For the diagonal from the upper right to the bottom left, the getDiagonal() function returns a list of tuples that the diagonal must have. In this direction, the numbers on the x axis start at 0 and increase until they reach the size of the board, while the numbers on the y axis go in reverse: they start at the size of the board and end at 0.</br>
Examples for each case in a 3x3 grid:

>[(0,**0**),(1,**0**),(2,**0**)] #First column complete wins</br>
[(**0**,0),(**0**,1),(**0**,2)] #First row complete wins</br>
[(**0,0**),(**1,1**),(**2,2**)] #Diagonal from upper left to bottom right wins</br>
[(**0**,*2*),(**1**,*1*),(**2**,*0*)] #diagonal from upper right to bottom left wins

The winner() function checks which player satisfies one of those conditions first.

The last important feature in project.py is when players click PLAY AGAIN. This button only appears if there is a winner or if the board is full with no winner. This function reverses the order of players to alternate which player starts in each round.

#### home.html
It is the page that lets the players choose their names and marks. They can also choose the size of the board, with options for a 3x3, 4x4, or 5x5 grid.

#### game.html:
Here the board is generated inside the HTML using nested loops, one for rows and one for columns. This is done using Jinja syntax. Each iteration assigns a coordinate to each cell. The first cell is (0,0), and it continues drawing and assigning coordinates until it reaches the size selected for the board.
The colors, names, marks, and scores are drawn according to the parameters passed from the server.</br>
Before drawing a cell, it checks if that cell is in any player's list to draw its corresponding mark and color. If not, it draws an empty clickable cell.

#### base.html
It is a template inherited by the other HTML documents.

#### Static files
Finally, in the static folder, there is the CSS stylesheet and the images to render on the board as marks for each player.

I hope this file will be helpful.
