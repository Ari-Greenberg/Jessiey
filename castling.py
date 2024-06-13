
import check
import global_variables
 # GHADY ABBOUD

def white_castling_valid(board_state, turn, init_loc, final_loc):
        # Check if it's a king side castle
    if board_state[init_loc] == 'K' and (final_loc - init_loc) == 2:
        if global_variables.white_king_moved or global_variables.white_rk_moved:
            return False
        # Check if the space between the king and the rook is empty
        if all(board_state[i] == '' for i in range(final_loc - 1, init_loc)):
            # Check if the king is not in check
            for i in range(init_loc,final_loc):
                board_state_copy = board_state[:]
                board_state_copy[i] = 'K'
                if check.in_check(board_state_copy, turn):
                    return False
            return True
        return False
    
        # Check if it's a queen side castle
    elif board_state[init_loc] == 'K' and (final_loc - init_loc) == -2:
        if global_variables.white_king_moved or global_variables.white_rq_moved:
            return False
        # Check if the space between the king and the rook is empty
        if all(board_state[i] == '' for i in range(final_loc - 1, init_loc - 1)):
        # Check if the king is in check
            for i in range(final_loc+1,init_loc+1):
                board_state_copy = board_state[:]
                board_state_copy[i] = 'K'
                if check.in_check(board_state_copy, turn):
                    return False
            return True

        return False


def black_castling_valid(board_state, turn, init_loc, final_loc):

        # Check if it's a king side castle
    if board_state[init_loc] == 'k' and (final_loc - init_loc) == 2:
        if global_variables.black_king_moved or global_variables.black_rk_moved:  # If the white king or rook have previously moved then can't castle
            return False
        # Check if the space between the king and the rook is empty
        if all(board_state[i] == '' for i in range(init_loc + 1, final_loc + 1)):
            # Check if the king is not in check
            for i in range(init_loc,final_loc):
                board_state_copy = board_state[:]
                board_state_copy[i] = 'k'
                if check.in_check(board_state_copy, turn):
                    return False
            return True
        
        return False
    
    elif board_state[init_loc] == 'k' and (final_loc - init_loc) == -2:
        if global_variables.black_king_moved or global_variables.black_rq_moved:
            return False
        # Check if the space between the king and the rook is empty
        if all(board_state[i] == '' for i in range(final_loc - 1, init_loc - 1)):
            # Check if the king is not in check
            for i in range(final_loc-1,init_loc):
                board_state_copy = board_state[:]
                board_state_copy[i] = 'k'
                if check.in_check(board_state_copy, turn):
                    return False
            return True

        return False