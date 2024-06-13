#Converts a piece in letter form to its number
piece_to_num = {
    "":0,
    "P":1,
    "N":2,
    "K":3,
    "R":4,
    "B":5,
    "Q":6,
    "p":9,
    "n":10,
    "k":11,
    "r":12,
    "b":13,
    "q":14,
}

num_to_p = ["","P","N","K","R","B","Q","x","x","p","n","k","r","b","q"]


#converts a letter board to its number form
def letters_to_num(board):
    board_list = []
    for item in board:
        if item.isupper():
            if item == "P":
                board_list.append(1)
            elif item == "N":
                board_list.append(2)
            elif item == "K":
                board_list.append(3)
            elif item == "R":
                board_list.append(4)
            elif item == "B":
                board_list.append(5)
            else:
                board_list.append(6)
        else:
            if item == "":
                board_list.append(0)
            elif item == "p":
                board_list.append(9)
            elif item == "n":
                board_list.append(10)
            elif item == "k":
                board_list.append(11)
            elif item == "r":
                board_list.append(12)
            elif item == "b":
                board_list.append(13)
            else:
                board_list.append(14)
    return board_list

def nums_to_lets(board):
    output_board = []
    for item in board:
        output_board.append(num_to_p[item])
    return output_board


#converts a letter board to its number form
def let_to_num(board):
    output_board = []
    for item in board:
        output_board.append(piece_to_num[item])
    return output_board

#generates a test board for testing purposes
def generate_test_board(board):
    for i in range(8):
        for j in range(8):
            print(f'{board[j+i*8]}{(" " if board[j+i*8]<10 else "")}', end=" ")
        print("\n")