import indicies_coordinate
import pygame

def pawn_move(board_state, turn, init_loc, final_loc,last_move):
    if init_loc == final_loc:
        return False
    piece_x, piece_y = indicies_coordinate.ind_to_coords(init_loc)
    final_x, final_y = indicies_coordinate.ind_to_coords(final_loc)
    if turn: #White Pawn
        if board_state[init_loc - 8] in ['K','Q','N','B','R','P','k','q','n','b','r','p']:
            if (board_state[(init_loc - 7)] in ['q','n','b','r','p']) and (board_state[(init_loc - 7)] == board_state[(final_loc)]):
                return True 
            elif (board_state[(init_loc - 9)] in ['q','n','b','r','p']) and (board_state[(init_loc - 9)] == board_state[(final_loc)]):                
                return True 
        # En Passant
        elif piece_y == 4 and (board_state[(init_loc - 1)] in ("p")) and (piece_y - 1 == final_y) and (piece_x - 1 == final_x) and (last_move[1] == final_loc-8) and (last_move[2] == final_loc+8):
            board_state[final_loc + 8] = ''
            return True
        elif piece_y == 4 and (board_state[(init_loc + 1)] in ("p")) and (piece_y - 1 == final_y) and (piece_x + 1 == final_x) and (last_move[1] == final_loc-8) and (last_move[2] == final_loc+8):
            board_state[final_loc + 8] = ''
            return True 
        # Regular Movement
        elif ((piece_y - 1 == final_y) and (piece_x == final_x)):
            return True
        elif (board_state[(init_loc - 7)] in ['q','n','b','r','p']) and (board_state[(init_loc - 7)] == board_state[(final_loc)]):
            return True 
        elif (board_state[(init_loc - 9)] in ['q','n','b','r','p']) and (board_state[(init_loc - 9)] == board_state[(final_loc)]):                
            return True 
        # Able to move 2 spaces off the start
        elif piece_y == 7: 
            if (board_state[init_loc - 8] in ['K','Q','N','B','R','P','k','q','n','b','r','p']) or (board_state[init_loc - 16] in ['K','Q','N','B','R','P','k','q','n','b','r','p']):
                return False
            elif ((piece_y - 1 == final_y) and (piece_x == final_x)) or ((piece_y - 2 == final_y) and (piece_x == final_x)):
                return True 
    else: #Black Pawn
        if board_state[init_loc + 8] in ['K','Q','N','B','R','P','k','q','n','b','r','p']:
            if (board_state[(init_loc + 7)] in ['Q','N','B','R','P']) and (board_state[(init_loc + 7)] == board_state[(final_loc)]):
                return True 
            elif (board_state[(init_loc + 9)] in ['Q','N','B','R','P']) and (board_state[(init_loc + 9)] == board_state[(final_loc)]):                
                return True 
            # En Passant 
        elif piece_y == 5 and (board_state[(init_loc - 1)] in ("P")) and (piece_y + 1 == final_y) and (piece_x - 1 == final_x) and (last_move[1] == final_loc+8) and (last_move[2] == final_loc-8):
            board_state[final_loc - 8] = ''
            return True
        elif piece_y == 5 and (board_state[(init_loc + 1)] in ("P")) and (piece_y + 1 == final_y) and (piece_x + 1 == final_x) and (last_move[1] == final_loc+8) and (last_move[2] == final_loc-8):
            board_state[final_loc - 8] = ''
            return True
         # Regular Movement
        elif ((piece_y + 1 == final_y) and (piece_x == final_x)):
            return True
        elif (board_state[(init_loc + 7)] in ['Q','N','B','R','P']) and (board_state[(init_loc + 7)] == board_state[(final_loc)]):
            return True 
        elif (board_state[(init_loc + 9)] in ['Q','N','B','R','P']) and (board_state[(init_loc + 9)] == board_state[(final_loc)]):                
            return True 
        # Able to move 2 spaces off the start
        elif piece_y == 2:
            if (board_state[init_loc + 8] in ['K','Q','N','B','R','P','k','q','n','b','r','p']) or (board_state[init_loc + 16] in ['K','Q','N','B','R','P','k','q','n','b','r','p']):
                return False
            elif ((piece_y + 1 == final_y) and (piece_x == final_x)) or ((piece_y + 2 == final_y) and (piece_x == final_x)):
                return True 
        else:
            return False 
    
