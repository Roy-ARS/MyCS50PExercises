from project import getDiagonal, winner, getColumnList, getRowList, getEqualPairs

def test_getDiagonal():
    assert getDiagonal(3) == [(0,2), (1,1), (2,0)]
    assert getDiagonal(2) == [(0,1), (1,0)]
    assert getDiagonal(4) == [(0,3), (1,2), (2,1), (3,0)]
    assert getDiagonal(5) == [(0,4), (1,3), (2,2), (3,1), (4,0)]

def test_winner():
    players1 = {"Player 1" : [(0,3), (1,2), (2,1), (3,0)], "Player 2" : [(0,1), (0,0), (1,0)]}
    players1B = {"Player 1" : [(0,2), (1,1), (1,2), (1,0)], "Player 2" : [(0,0), (2,2), (2,0)]}
    players2 = {"Player 1" : [(0,1), (0,2), (1,2)], "Player 2" : [(0,0), (1,0), (2,0)]}
    players2B = {"player 1" : [(0,2), (3,0), (1,2), (1,0), (3,2), (2,3)], "Player 2" : [(0,0), (2,2), (2,0), (1,1), (1,3), (3,3)]}
    playersNone = {"Player 1" : [(2,1), (1,2), (1,0), (0,1)], "Player 2" : [(0,0), (2,2), (2,0)]}
    assert winner(4, players1) == "Player 1" #In this dict the player 1 has a diagonal of 4 cells
    assert winner(3, players1B) == "Player 1" #In this dict the player 1 has a horizontal line of 3 cells
    assert winner(3, players2) == "Player 2" #In this dict the player 2 has a vertical line of 3 cells
    assert winner(4, players2B) == "Player 2" #In this dict the player 2 has a diagonal of 4 cells
    assert winner(5, players1) == None #In this dict player 1 has a diagonal of 4 cells, but the passed size parameter is 5
    assert winner(3, playersNone) == None #In this dict none of the player has the requirements to win yet

#same lists for next tests
player1 = [(0,1),(0,2),(0,0)]
player2 = [(1,0),(8,1),(3,2),(0,2)]
player3 = [(1,2),(1,1),(3,3),(0,2),(7,7)]
def test_getColumnList():
    assert getColumnList(player1) == [1,2,0]
    assert getColumnList(player2) == [0,1,2,2]
    assert getColumnList(player3) == [2,1,3,2,7]

def test_getRowList():
    assert getRowList(player1) == [0,0,0]
    assert getRowList(player2) == [1,8,3,0]
    assert getRowList(player3) == [1,1,3,0,7]

def test_getEqualPairs():
    assert getEqualPairs(player1) == 1
    assert getEqualPairs(player2) == 0
    assert getEqualPairs(player3) == 3