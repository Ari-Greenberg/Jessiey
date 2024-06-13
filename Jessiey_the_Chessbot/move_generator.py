if __name__ == "__main__":
    import move_piece
    import board_eval
    import board_conversions
else:
    from Jessiey_the_Chessbot import move_piece
    from Jessiey_the_Chessbot import board_eval
    from Jessiey_the_Chessbot import board_conversions


#Stores board data at each index
piece_data = []
#stores dirrectionns used for movement
king_dirrections = {9,8,7,1,-1,-7,-8,-9}
knight_dirrections = {17,15,10,6,-6,-10,-15,-17}
knight_dirrections_coords = [(2,1),(1,2)]

#saved data used for calculations
class board_data:
    def __init__(self, index):
        self.index = index
        self.rank = self.index//8 + 1
        self.file = self.index%8 + 1
        self.from_top = self.rank - 1
        self.from_bot = 8 - self.rank
        self.from_left = self.file - 1
        self.from_right = 8 - self.file
#connects board data to piece data
def create_board_data():
    for i  in range(64):
        piece_data.append(board_data(i))


#saves a move as everything you would need to know about about
class moves:
    def __init__(self, piece, previous_loc, final_loc, other_pre=-3, other_final=0):
        self.piece = piece
        self.player = True if piece < 8 else False
        self.previous_loc = previous_loc
        self.final_loc = final_loc
        self.other_pre = other_pre #-1 if a white pawn promotion, -2 if a black pawn promotion, -3 if nothing
        self.other_final = other_final #-1 if piece is just being removed
        self.eval = None
        self.c_rights = None

# Castling order Represent White Kingside, White Queenside, Black Kingside, Black Queenside
def generate_moves(board, turn, l_move, castling_rights):
    moves_list = []
    #turns last move into a tuple
    last_move = (l_move.piece,l_move.previous_loc,l_move.final_loc)
    #mirrored versions of code based on turn
    if turn:
        #for each piece on the board of the current players color, add all posible moves to the moves list
        for index, piece in enumerate(board):
            if piece != 0:
                if piece == 1: #White Pawn Moves
                    one_in_front = index-8
                    two_in_front = index-16
                    if board[one_in_front] == 0:
                        if piece_data[index].rank == 7:
                            moves_list.append(moves(1,index,one_in_front))
                            if board[two_in_front] == 0:
                                moves_list.append(moves(1,index,two_in_front))
                        else:
                            if piece_data[one_in_front].rank == 1:
                                moves_list.append(moves(2,index,one_in_front,-1))
                                moves_list.append(moves(4,index,one_in_front,-1))
                                moves_list.append(moves(5,index,one_in_front,-1))
                                moves_list.append(moves(6,index,one_in_front,-1))
                            else:
                                moves_list.append(moves(1,index,one_in_front))
                    for diagonal in [-9,-7]:
                        new_index = index+diagonal
                        if board[new_index]>8 and abs(piece_data[new_index].file-piece_data[index].file) == 1:
                            moves_list.append(moves(1,index,new_index))
                        else:
                            if last_move[0] == 9:
                                if last_move[2]-last_move[1] == 16:
                                    if new_index == last_move[1]+8 and abs(piece_data[new_index].file-piece_data[index].file) == 1:
                                        moves_list.append(moves(1,index,new_index,last_move[2],-1))
                elif piece == 3: #White King Moves
                    for offset in king_dirrections:
                        new_index = index+offset
                        if 64 > new_index >= 0:
                            if (abs(piece_data[new_index].file-piece_data[index].file) in (0,1) and abs(piece_data[new_index].rank-piece_data[index].rank) in (0,1)):
                                if not 0<board[new_index]<8:
                                    moves_list.append(moves(3,index,new_index))
                    if castling_rights[0]:
                        blocked = False
                        for i in [61,62]:
                            if board[i] != 0:
                                blocked = True
                        if not blocked:
                            moves_list.append(moves(3,60,62,63,61))
                    if castling_rights[1]:
                        blocked = False
                        for i in [59,58,57]:
                            if board[i] != 0:
                                blocked = True
                        if not blocked:
                            moves_list.append(moves(3,60,58,56,59))
                elif piece == 2: #White Knight Moves
                    for offset in knight_dirrections:
                        new_index = index+offset
                        if 64 > new_index >= 0:
                            if (abs(piece_data[new_index].file-piece_data[index].file),abs(piece_data[new_index].rank-piece_data[index].rank)) in knight_dirrections_coords:
                                if not 0<board[new_index]<8:
                                    moves_list.append(moves(2,index,new_index))
                elif piece == 4: #White Rook Moves
                    for dist in range(1, piece_data[index].from_top+1):
                        new_index = index-8*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(4,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_bot+1):
                        new_index = index+8*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(4,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_left+1):
                        new_index = index-1*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(4,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_right+1):
                        new_index = index+1*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(4,index,new_index))
                            if board[new_index] != 0:
                                break
                elif piece == 5: #White Bishop Moves
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_left)+1):
                        new_index = index-9*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(5,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_left)+1):
                        new_index = index+7*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(5,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_right)+1):
                        new_index = index+9*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(5,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_right)+1):
                        new_index = index-7*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(5,index,new_index))
                            if board[new_index] != 0:
                                break
                elif piece == 6: #White Queen Moves                  
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_left)+1):
                        new_index = index-9*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_left)+1):
                        new_index = index+7*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_right)+1):
                        new_index = index+9*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_right)+1):
                        new_index = index-7*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_top+1):
                        new_index = index-8*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_bot+1):
                        new_index = index+8*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_left+1):
                        new_index = index-1*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_right+1):
                        new_index = index+1*dist
                        if 0<board[new_index]<8:
                            break
                        else:
                            moves_list.append(moves(6,index,new_index))
                            if board[new_index] != 0:
                                break
    else:
        for index, piece in enumerate(board):
            if piece != 0:
                if piece == 9: #Black Pawn Moves
                    one_in_front = index+8
                    two_in_front = index+16
                    if board[one_in_front] == 0:
                        if piece_data[index].rank == 2:
                            moves_list.append(moves(9,index,one_in_front))
                            if board[two_in_front] == 0:
                                moves_list.append(moves(9,index,two_in_front))
                        else:
                            if piece_data[one_in_front].rank == 8:
                                moves_list.append(moves(10,index,one_in_front,-2))
                                moves_list.append(moves(12,index,one_in_front,-2))
                                moves_list.append(moves(13,index,one_in_front,-2))
                                moves_list.append(moves(14,index,one_in_front,-2))
                            else:
                                moves_list.append(moves(9,index,one_in_front))
                    for diagonal in [7,9]:
                        new_index = index+diagonal
                        if 0<board[new_index]<8 and abs(piece_data[new_index].file-piece_data[index].file) == 1:
                            moves_list.append(moves(9,index,new_index))
                        else:
                            if last_move[0] == 1:
                                if last_move[1]-last_move[2] == 16:
                                    if new_index == last_move[1]-8 and abs(piece_data[new_index].file-piece_data[index].file) == 1:
                                        moves_list.append(moves(9,index,new_index,last_move[2],-1))
                elif piece == 11: #Black King Moves
                    for offset in king_dirrections:
                        new_index = index+offset
                        if 64 > new_index >= 0:
                            if (abs(piece_data[new_index].file-piece_data[index].file) in (0,1) and abs(piece_data[new_index].rank-piece_data[index].rank) in (0,1)):
                                if  board[new_index]<8:
                                    moves_list.append(moves(11,index,new_index))
                    if castling_rights[2]:
                        blocked = False
                        for i in [5,6]:
                            if board[i] != 0:
                                blocked = True
                        if not blocked:
                            moves_list.append(moves(11,4,6,7,5))
                    if castling_rights[3]:
                        blocked = False
                        for i in [3,2,1]:
                            if board[i] != 0:
                                blocked = True
                        if not blocked:
                            moves_list.append(moves(11,4,2,0,3))
                elif piece == 10: #Black Knight Moves
                    for offset in knight_dirrections:
                        new_index = index+offset
                        if 64 > new_index >= 0:
                            if (abs(piece_data[new_index].file-piece_data[index].file),abs(piece_data[new_index].rank-piece_data[index].rank)) in knight_dirrections_coords:
                                if board[new_index]<8:
                                    moves_list.append(moves(10,index,new_index))
                elif piece == 12: #Black Rook Moves
                    for dist in range(1, piece_data[index].from_top+1):
                        new_index = index-8*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(12,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_bot+1):
                        new_index = index+8*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(12,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_left+1):
                        new_index = index-1*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(12,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_right+1):
                        new_index = index+1*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(12,index,new_index))
                            if board[new_index] != 0:
                                break
                elif piece == 13: #Black Bishop Moves
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_left)+1):
                        new_index = index-9*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(13,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_left)+1):
                        new_index = index+7*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(13,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_right)+1):
                        new_index = index+9*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(13,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_right)+1):
                        new_index = index-7*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(13,index,new_index))
                            if board[new_index] != 0:
                                break
                elif piece == 14: #Black Queen Moves
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_left)+1):
                        new_index = index-9*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_left)+1):
                        new_index = index+7*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_bot,piece_data[index].from_right)+1):
                        new_index = index+9*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, min(piece_data[index].from_top,piece_data[index].from_right)+1):
                        new_index = index-7*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_top+1):
                        new_index = index-8*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_bot+1):
                        new_index = index+8*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_left+1):
                        new_index = index-1*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
                    for dist in range(1, piece_data[index].from_right+1):
                        new_index = index+1*dist
                        if board[new_index]>8:
                            break
                        else:
                            moves_list.append(moves(14,index,new_index))
                            if board[new_index] != 0:
                                break
    return moves_list

def get_legal_moves(board, turn, last_move, castling_rights):
    moves = generate_moves(board, turn, last_move, castling_rights)
    legal_moves = []
    for move in moves:
        move.eval = board_eval.eval(board, turn, last_move, castling_rights)
        valid = True
        new_board, move, new_castling_rights, old_board = move_piece.make_move(board, move, castling_rights[:])
        move.c_rights = new_castling_rights
        opponent_moves = generate_moves(board, not turn, move, new_castling_rights)
        if len(opponent_moves) > 0:
            if move.other_final > 0:
                if move.other_final == 61:
                    cross_squares = {61,62}
                elif move.other_final == 59:
                    cross_squares = {59,58,57}
                elif move.other_final == 5:
                    cross_squares = {5,6}
                elif move.other_final == 3:
                    cross_squares = {3,2,1}
                for o_move in opponent_moves:
                    if (o_move.final_loc in cross_squares):
                        valid = False
                        break
        if valid:
            if not check(new_board, turn, move, move.c_rights):
                legal_moves.append(move)
    return legal_moves

#checks if current player is in check
def check(board, turn, last_move, castling_rights):
        opponent_moves = generate_moves(board, not turn, last_move, castling_rights)
        in_check = False
        if len(opponent_moves) > 0:
            for o_move in opponent_moves:
                if board[o_move.final_loc] == (3 if turn else 11):
                    in_check = True
                    break
        return in_check

#insert board state, player move, and last move made
#0 means nobody is in checkmate, 1 means white wins, 2 means black wins, 3 means the game ends in a stalemate.
def checkmate(board,turn,last_move):
    print("\nChecking for mate")
    mvs = get_legal_moves(board, turn, last_move,last_move.c_rights)
    if len(mvs) == 0:
        if check(board,turn,last_move,last_move.c_rights):
            if turn:
                return 2
            else:
                return 1
        else:
            return 3
    else:
        return 0
    
create_board_data()
         