import bishop
import knights
import rook
import pawn
import king
import indicies_coordinate
import castling

def move_check(board_state, turn, init_loc, final_loc,last_move):
    piece = board_state[init_loc]
    if ((piece in ['K','Q','N','B','R','P']) and (not turn)) or ((piece in ['k','q','n','b','r','p']) and turn): #Check if piece matches turn
        return False
    elif piece.lower() == "b": # Check if piece is a bishop
        return bishop.bishop_moveable(board_state, turn, init_loc, final_loc)
    elif piece.lower() == "n": # Check if piece is a knight
        return knights.knight_moveable(board_state, turn, init_loc, final_loc)
    elif piece.lower() == "r": # Check if piece is a rook
        return rook.rook_moveable(board_state, turn, init_loc, final_loc)
    elif piece.lower() == "q": # Check if piece is a queen
        return bishop.bishop_moveable(board_state, turn, init_loc, final_loc) or rook.rook_moveable(board_state, turn, init_loc, final_loc)
    elif piece.lower() == "p": # Check if piece is a pawn
        return pawn.pawn_move(board_state, turn, init_loc, final_loc,last_move)
    elif piece.lower() == "k": # Check if piece is a king
        if (abs(final_loc - init_loc) == 2) or (abs(final_loc-init_loc) == 4):
            if turn:
                return castling.white_castling_valid(board_state, turn, init_loc, final_loc)
            else:
                return castling.black_castling_valid(board_state, turn, init_loc, final_loc)
        return king.king_moveable(board_state, turn, init_loc, final_loc)