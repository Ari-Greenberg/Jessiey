#makes a move and returns the result after the move
def make_move(board, move, castling_rights):
    #creates a new board state and moves the piece
    new_board_state = board.copy()
    new_board_state[move.final_loc] = move.piece
    new_board_state[move.previous_loc] = 0
    #Modifies castling rights as neccesary
    if move.piece == 3:
        castling_rights[0], castling_rights[1] = False,False
    elif move.piece == 11:
        castling_rights[2], castling_rights[3] = False,False
    elif move.previous_loc == 63 or move.final_loc == 63:
        castling_rights[0] = False
    elif move.previous_loc == 56 or move.final_loc == 56:
        castling_rights[1] = False
    elif move.previous_loc == 0 or move.final_loc == 0:
        castling_rights[3] = False
    elif move.previous_loc == 7 or move.final_loc == 7:
        castling_rights[2] = False
    #if performing en pessant or castling, removes other pawn, or moves rook
    if move.other_pre >= 0:
        if move.other_final != -1:
            new_board_state[move.other_final] = board[move.other_pre]
        new_board_state[move.other_pre] = 0
    return (new_board_state, move, castling_rights, board)