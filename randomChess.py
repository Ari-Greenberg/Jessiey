#file that contains random board state chess variant code
import random

def randomBoard():
    #['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 
    # 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 
    # '', '', '', '', '', '', '', '', 
    # '', '', '', '', '', '', '', '', 
    # '', '', '', '', '', '', '', '', 
    # '', '', '', '', '', '', '', '',
    # 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 
    # 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    otherSide = []
    boardState = []
    #make and append one side of the board
    for i in range(16):
        if i != 4:
            boardState.append(random.choice('rnbqbnrp'))
        else:
            boardState.append('k')
    #add filler space
    for i in range(32):
        boardState.append('')
    #make and append the other side of the board
    for i in boardState[8:16]:
        boardState.append(i.upper())
    for i in boardState[0:8]:
        boardState.append(i.upper())
    return boardState
    

#main section meant for some basic testing
if __name__ == '__main__':
    for i in range (12):
        print(random.choice('rnbqkbnrp'))
    print(randomBoard())