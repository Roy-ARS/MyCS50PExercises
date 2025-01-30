from flask import Flask, render_template, url_for, request, redirect
from collections import OrderedDict
#Made by Roy Rodriguez Segura
#GitHub user: Roy-ARS

app = Flask(__name__)

playersG = {}  #{"name" : [(n,n),(n1,n1)...]} tuples containing board cells owned by each player
playerWinsG = {} #{"name" : n, ...} number of wins for each player
symbolsG = {} #{"name" : ("img_n.png", "(r, g, b)"), ...} symbol selected by each player, and asign a color
sizeG = 3  #size of the board default to standard 3x3
winnerG = "" #name of the winner for each round

def main():
    app.run(debug=True)

@app.route("/player1", methods=["POST", "GET"])
def player1():
    name = list(playersG.keys())[0] #gets the name of the player 1
    return playTurn(1, name)

@app.route("/player2", methods=["POST", "GET"])
def player2():
    name = list(playersG.keys())[1] #gets the name of the player 2
    return playTurn(2, name)


############this method is called from playTurn() when a player satisfies a condition to win
@app.route("/winner_is", methods=["POST", "GET"])
def winner_is():
    global playersG
    global symbolsG
    global playerWinsG
    if request.method == "POST":
        if request.form.get("box") == "PLAY AGAIN":
            return playAgain()
        elif request.form.get("box") == "HOME":
            return redirect(url_for("home"))
    else:
        return render_template("game.html", winner=True, #winner=True triggers the CONGRATULATIONS text, and disable cells
                                   playerWins=playerWinsG,
                                   symbols=symbolsG,
                                   size=sizeG,
                                   playerName = winnerG,
                                   players=playersG,
                                   player1Name=list(playersG.keys())[0],
                                   player2Name=list(playersG.keys())[1])


###########this method is called to verify the maximun wins for a player
# to reset the winner for another round
# and it inmediatly redirects to player 1 turn or home, dependign on max wins for a player
@app.route("/game")
def game():
    global winnerG
    winnerG = None
    maxReached = False
    for player in playersG:
        if playerWinsG[player] >= 99:  #limit of wins for one player
            maxReached = True
            break
    if maxReached:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("player1"))


############### The home page where players choose names and select their symbols
@app.route("/", methods=["POST", "GET"])
def home():
    global playersG
    global sizeG
    global symbolsG
    global playerWinsG
    #everything is cleared on this page
    color1 = "(240, 175, 40)" #passed to the style of the HTML
    color2 = "(75, 140, 190)" #passed to the style of the HTML
    playersG = {}
    sizeG = 3
    symbolsG = {}
    playerWinsG = {}
    #default names
    name1 = "Player 1"
    name2 = "Player 2"

    if request.method == "POST":
        sizeG = int(request.form.get("size")) #sets the given size of the board

        #Next lines get default name if name is not given, or sets the given name
        if request.form.get("player1Name") == "" and request.form.get("player2Name") == "":
            playersG = OrderedDict({name1 : [], name2 : []}) #if neither player gave a name
        elif request.form.get("player1Name") == "":
            playersG = OrderedDict({name1 : [], request.form.get("player2Name") : []}) #if only player 2 gave a name
        elif request.form.get("player2Name") == "":
            playersG = OrderedDict({request.form.get("player1Name") : [], name2 : []}) #if only player 1 gave a name
        else:
            print(f"REQUEST NAME {request.form.get("player1Name")}") #if both players gave a name
            playersG = OrderedDict({request.form.get("player1Name") : [], request.form.get("player2Name") : []})

        #Next lines get the default images or the images selected by the players
        #default symbols are the classical X and O
        if request.form.get("imageP1") == None and request.form.get("imageP2") == None:
            symbolsG = OrderedDict({list(playersG.keys())[0] : ("Default_1.png", color1),
                       list(playersG.keys())[1] : ("Default_2.png", color2)}) #if neither player selected a symbol
        elif request.form.get("imageP1") == None:
            symbolsG = OrderedDict({list(playersG.keys())[0] : ("Default_1.png", color1),
                       list(playersG.keys())[1] : (request.form.get("imageP2"), color2)}) #only player 2 selected a symbol
        elif request.form.get("imageP2") == None:
            symbolsG = OrderedDict({list(playersG.keys())[0]: (request.form.get("imageP1"), color1),
                       list(playersG.keys())[1] : ("Default_2.png", color2)}) #only player 1 selected a symbol
        else:
            symbolsG = OrderedDict({list(playersG.keys())[0] : (request.form.get("imageP1"), color1),
                      list(playersG.keys())[1] : (request.form.get("imageP2"), color2)}) #both players selected a symbol
        playerWinsG = {list(playersG.keys())[0] : 0,
                       list(playersG.keys())[1] : 0} #sets the playerWins dict to the names given and resets to 0
        return redirect(url_for("game"))
    return render_template("home.html")


###############before starting again, this reverses the players order and clears the cells
#              then returns to game page
def playAgain():
    global playersG
    playersG = OrderedDict({list(playersG.keys())[1] : [],
                list(playersG.keys())[0]: []})
    return redirect(url_for("game"))


############## This is the method called to verify if a player has won
#### it works no matter the size of the board passed as a parameter
def winner(size, players):
    #in tic tac toe the winner is triggered when he satisfies one of three conditions:
    # 1- he has owned a whole column, that means the y value of his set of tuples are the same
    # 2- he has owned a whole row, that means the x value of his set of tuples are the same
    # 3- he has owned a diagonal
    #   3.1- from upper left to bottom right each tuple must have the same number in both values (x,y)
    #   3.2- from upper right to bottom left, the numbers in x must be increasing, and in y must be decreasing
    # a winner is returned if one of those conditions is satisfied for the amount of tuples equal to the size of the game
    diagonalList = getDiagonal(size)
    for player in players:
        columnList = getColumnList(players[player])  #list of columns owned by player
        rowList = getRowList(players[player])  #list of rows owned by the player
        equalPairs = getEqualPairs(players[player]) #amount of tuples that has same values
        countDiagonal = 0
        for t in diagonalList:
            if t in players[player]:
                countDiagonal += 1
        if countDiagonal == size: #winner is returned if the diagonal cells the player has equals the size of the board
            return player
        if equalPairs == size:  #winner is returned when player has {size} x and y equal pairs (diagonal from top left to righ bottom)
            return player
        for x in rowList:
            if rowList.count(x) == size:  #winner is returned if player owns all cells available in the same row
                return player
        for y in columnList:
            if columnList.count(y) == size:  #winner is returned if player owns all columns available in the same column
                return player
    return None

def getColumnList(player): #gets the numbers of the columns of player's list
    columnList = []
    for tuple in player:
        columnList.append(tuple[1])
    return columnList

def getRowList(player): #gets the numbers of the rows of player's list
    rowList = []
    for tuple in player:
        rowList.append(tuple[0])
    return rowList

def getEqualPairs(player): #gets the amount of tuples that has the same values
    equals = 0
    for tuple in player:
        if tuple[0] == tuple[1]:
            equals += 1
    return equals


############ This is the turn for each player
def playTurn(num, pName):
    global playersG
    global winnerG
    global symbolsG
    global playerWinsG
    cellList = playersG[pName]
    if num == 1:
        newUrl = "player2"  #if it's player 1's turn, redirect to player 2's turn
    else:
        newUrl = "player1"  #if it's player 2's turn, redirect to player 1's turn
    if winner(sizeG, playersG) == None:
        if request.method == "POST":
            if request.form.get("box") == "PLAY AGAIN":
                return playAgain()
            elif request.form.get("box") == "HOME":
                return redirect(url_for("home"))
            else: #checks what cell is clicked
                cell = request.form.get("box")
                x, y = cell.split(",")
                cellList.append((int(x), int(y)))
                playersG[pName] = cellList
                return redirect(url_for(newUrl))
        else:
            return render_template("game.html", winner=False,
                                   playerWins=playerWinsG,
                                   symbols=symbolsG,
                                   size=sizeG,
                                   playerName = pName,
                                   players=playersG,
                                   player1Name=list(playersG.keys())[0],
                                   player2Name=list(playersG.keys())[1])
    else:
        winnerG = winner(sizeG, playersG)
        playerWinsG[winnerG] += 1
        return redirect(url_for("winner_is"))

def getDiagonal(size):
    #returns a list of the total tuples values that the diagonal from upper right to bottom left must have
    #(x,y) in such diagonal line, x must be increasing from 0 to size-1 and y must be decreasing from size-1 to 0
    diagonal = []
    for i in range(size):
        diagonal.append((i, size-1-i))
    return diagonal

if __name__ == "__main__":
    main()
