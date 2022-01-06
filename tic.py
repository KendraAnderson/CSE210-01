#Assignment 'Tic Tac Toe'
#Authors: Kendra Anderson
#1-5-2022

#create variables
x = 'X'
o = 'O'
xColor = '#03fcd7'
oColor = '#0390fc'
winnerColor = '#fc1c03'
turn = 1

#create board list
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#create end of game boolean
endOfGame = False



#print board
def printBoard():
    print("\n")
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("--+---+--")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("--+---+--")
    print("{} | {} | {}".format(board[6], board[7], board[8]))
    #print("\n")

#get input
#def getInput():
    
    #input("First player choose where to put your X (1-9)")
    #call change board?

#change board index value
#def changeBoard():

#check for end of game
#def endGame():
    #check for 3 in a row
    #check for full board
    #for i in board:
        #if board[i] == i + 1:
         #   continue
        #else:
         #   endOfGame = True
    #print("game over")     
     
def main():
    print("Time for Tic Tac Toe!")
    #call print board
    printBoard()    

    #while endOfGame == False:
        #call get input
        #getInput()
        #call print board
        #printBoard()
        #call check for end of game
        #endGame()

if __name__ == "__main__":
    main()