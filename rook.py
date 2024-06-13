import indicies_coordinate
import global_variables

def rook_moveable(board_state, turn, init_loc, final_loc):
    
    #does the basic check for piece of similar color and different space check
    not_takeable = (board_state[final_loc] in (['K','Q','N','B','R','P'] if turn else ['k','q','n','b','r','p']))
    if init_loc == final_loc or not_takeable:
        return False
    #establishes coordinates for later use
    piece_x, piece_y = indicies_coordinate.ind_to_coords(init_loc)
    final_x, final_y = indicies_coordinate.ind_to_coords(final_loc)
    #checks if the final location is in line on either the x or y axis 
    if (piece_x != final_x) and (piece_y != final_y):
        return False
    #checks interference, first be establishing which axis is in-line then running through each space between current and final
    #position and checking to make sure it is empty. It does this by either incrementing or decrementing depending
    if piece_x == final_x:
        for i in range(1, abs(final_y - piece_y)):
            if (final_y > piece_y):
                if board_state[indicies_coordinate.coords_to_ind(piece_x, piece_y + i)] in ['K','Q','N','B','R','P','k','q','n','b','r','p']:
                    return False
            else:
                if board_state[indicies_coordinate.coords_to_ind(piece_x, piece_y - i)] in ['K','Q','N','B','R','P','k','q','n','b','r','p']:
                    return False
    if piece_y == final_y:
        for i in range(1, abs(final_x - piece_x)):
            if (final_x > piece_x):
                if board_state[indicies_coordinate.coords_to_ind(piece_x + i, piece_y)] in ['K','Q','N','B','R','P','k','q','n','b','r','p']:
                    return False
            else:
                if board_state[indicies_coordinate.coords_to_ind(piece_x - i, piece_y)] in ['K','Q','N','B','R','P','k','q','n','b','r','p']:
                    return False

    return True
    
    