import indicies_coordinate
import global_variables

white_king_moved = False
black_king_moved = False

def king_moveable(board_state, turn, init_loc, final_loc):
    #does the basic check for piece of similar color and different space check
    not_takeable = (board_state[final_loc] in (['K','Q','N','B','R','P'] if turn else ['k','q','n','b','r','p']))
    if init_loc == final_loc or not_takeable:
        return False
    #establishes coordinates for later use
    piece_x, piece_y = indicies_coordinate.ind_to_coords(init_loc)
    final_x, final_y = indicies_coordinate.ind_to_coords(final_loc)
    #checks if final location is within one space of the initial location
    if (abs(final_y - piece_y) > 1) or (abs(final_x - piece_x) > 1):
        return False
    return True
