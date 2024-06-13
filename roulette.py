import random
import indicies_coordinate

def roulette(board_state, init_loc, final_loc,last_move):
    fatal_shot = random.randint(1, 6)
    shot_taken = random.randint(1, 6)
    if last_move == ((("P") or ("p") or ("B") or ("b") or ("Q") or ("q") or ("N") or ("n")),range(0,63),range(0,63)):
            if shot_taken == fatal_shot:
                board_state[final_loc] = ''
            
