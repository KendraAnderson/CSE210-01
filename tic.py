#Assignment 'Tic Tac Toe'
#Authors: Kendra Anderson
#1-5-2022

#print board
def printBoard(board):
    
    print("\n")
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("--+---+--")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("--+---+--")
    print("{} | {} | {}".format(board[6], board[7], board[8]))
    print("\n")

#get input
def getInput(turn, board):
    
    value = 0

    if turn % 2 == 0:
        value = getX()
        symbol = 'X'
        board = changeValue(value, symbol, board)
    elif turn % 2 != 0:
        value = getO()
        symbol = 'O'
        board = changeValue(value, symbol, board)
    
    return board

def getX():
    
    value = 0

    while (value < 1 or value > 9):
        value = int(input("First player choose where to put your X. Choose a number 1 - 9: "))
    
    return value

def getO():
    
    value = 0

    while (value < 1 or value > 9):
        value = int(input("Second player choose where to put your O. Choose a number 1 - 9: "))
    
    return value

#change board index value
def changeValue(value, symbol, board):
    board[value - 1] = symbol
    return board

#check for end of game
def checkEnd(board):
    
    #check for 3 in a row
    winner = checkWinner(board)
    
    #check for full board
    if ((board[0] == 'X' or board[0] == 'O') and
    (board[1] == 'X' or board[1] == 'O') and
    (board[2] == 'X' or board[2] == 'O') and
    (board[3] == 'X' or board[3] == 'O') and
    (board[4] == 'X' or board[4] == 'O') and
    (board[5] == 'X' or board[5] == 'O') and
    (board[6] == 'X' or board[6] == 'O') and
    (board[7] == 'X' or board[7] == 'O') and
    (board[8] == 'X' or board[8] == 'O') or
    winner == 'X' or winner == "O" or winner == 'nobody'):
        farewell = winner + ' is the winner. Thank you for playing.'
        print(farewell)
        return True
    else:
        return False
    
def checkWinner(board):
    
    winner = 'Not End'

    if ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or
    (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or
    (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or
    (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or
    (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or
    (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or
    (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or
    (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
        winner = 'X'
    elif ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or
    (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or
    (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or
    (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or
    (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or
    (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or
    (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or
    (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
        winner = 'O'
    else:
        winner = 'Nobody'
    
    
    
    return winner
     
def main():
    
    #Create board list
    board = ['1','2','3','4','5','6','7','8','9']
    
    #create end boolean
    end = False
    
    turn = 2

    print("Time for Tic Tac Toe!")
    #call print board
    printBoard(board)    

    while end != True:
        
        #call get input
        board = getInput(turn, board)
        
        #call print board
        printBoard(board)
        
        #call check for end of game
        end = checkEnd(board)

        turn += 1

if __name__ == "__main__":
    main()