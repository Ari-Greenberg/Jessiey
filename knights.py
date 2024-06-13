import indicies_coordinate

def knight_moveable(board_state, turn, init_loc, final_loc): # Checks if a knight can move from init_loc to final_loc

    moves = [(1,2), (-1,2), (2, -1), (-2, -1), (-1, -2), (1, -2), (-2, 1), (2, 1)]

    # Check if the destination square is occupied by a friendly piece
    friendly_pieces = ['K','Q','N','B','R','P'] if turn else ['k','q','n','b','r','p']
    if board_state[final_loc] in friendly_pieces:
        return False

    # Check if the move is found in the moves list.

    init_x, init_y = indicies_coordinate.ind_to_coords(init_loc)
    final_x, final_y = indicies_coordinate.ind_to_coords(final_loc)
    dx = final_x - init_x
    dy = final_y - init_y
    if (dx,dy) in moves:
        return True
    
    return False