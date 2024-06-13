import indicies_coordinate

#takes in current board space, current player turn, current bishop location,
#and the place you want to move the bishop to return whether or not the
#bishop can move there

def bishop_moveable(board_state, turn, init_loc, final_loc):
    not_takeable = (board_state[final_loc] in (['K','Q','N','B','R','P'] if turn else ['k','q','n','b','r','p']))
    if init_loc == final_loc or not_takeable:
        return False
    piece_x, piece_y = indicies_coordinate.ind_to_coords(init_loc)
    final_x, final_y = indicies_coordinate.ind_to_coords(final_loc)
    dx = piece_x - final_x
    dy = piece_y - final_y
    positive_dx = abs(dx)
    positive_dy = abs(dy)
    if positive_dx != positive_dy:
        return False
    interferance = False
    if positive_dx > 1:
        for i in range(positive_dx-1):
            if board_state[indicies_coordinate.coords_to_ind(piece_x + (i+1)*(-1 if dx > 0 else 1),piece_y + (i+1)*(-1 if dy > 0 else 1))] in ['K','Q','N','B','R','P','k','q','n','b','r','p']:
                interferance = True
    if interferance:
        return False
    else:
        return True
