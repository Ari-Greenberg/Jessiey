if __name__ == "__main__":
    import board_conversions
    import move_generator
    import board_eval
    import move_piece
else:
    from Jessiey_the_Chessbot import board_conversions
    from Jessiey_the_Chessbot import move_generator
    from Jessiey_the_Chessbot import board_eval
    from Jessiey_the_Chessbot import move_piece
import math
import time

#Piece type chart
# 1 - pawn , 2 - knight , 3 - king , 4 - rook , 5 - bishop , 6 - queen. +8 if black
#True for white, False for black
#board state is a list of 64 numbers where each is a number (0 for empty)
#A move is a an object

#b = ['r','n','b','','k','b','n','r','p','p','p','p','p','p','p','p','','','B','','','','','','','','','','','','','','','','','','','','','','','','','','','','','q','P','P','P','P','P','P','P','P','R','N','','Q','K','B','N','R']

#used to quickly evaluate the quality of a move
quick_eval = [0,1,3,15,5,3,9,0,0,1,3,15,5,3,9]

#Checks for best move based on depth
def best_move(board, turn, depth, alpha, beta, last_move):
    #If the end of the tree is reached, get the eval of the board
    if depth == 0:
        return board_eval.eval(board,turn,last_move,last_move.c_rights), 0
    else:
        #gets a list of all legal moves
        moves = move_generator.get_legal_moves(board, turn, last_move,last_move.c_rights)
        #if there are no legal moves, returns an eval for win, loss, or stalemate
        if len(moves) == 0:
            if move_generator.check(board, turn, last_move, last_move.c_rights):
                if turn:
                    return -20000, last_move
                else:
                    return 20000, last_move
            else:
                return 0, last_move
        else:
            #If there are moves, this sorts them based on what piece you are taking, and what piece you are using to take it
            #ex: queen taking a pawn has a -8 sort value. Pawn taking a queen has a +8 sort value
            #This makes pruning more efficient later
            if depth > 1:
                moves.sort(reverse=True,key=lambda move: ((quick_eval[board[move.final_loc]] - quick_eval[move.piece]) if board[move.final_loc] != 0 else 0))
            best = moves[0]
            #mirrored versions of the code based on who's turn it is
            if turn:
                for move in moves:
                    #For each move, we make the move on a test board, Then we recursively run best_move on it
                    new_board_state, move, new_castling_rights, board = move_piece.make_move(board, move, last_move.c_rights)
                    move.c_rights = new_castling_rights
                    rating = best_move(new_board_state, not turn, depth-1, alpha, beta, move)[0]
                    move.eval = rating
                    #We set the moves eval to the rating determined through recursion
                    #then we return the best move possible for the current player, along with its eval
                    #Alpha and beta are used to stop evaluating moves that will never be used, because they are too good for the opponent
                    if alpha < move.eval:
                        alpha = move.eval
                        best = move
                    if alpha >= beta:
                        return alpha, best
                return alpha, best
            else:
                for move in moves:
                    new_board_state, move, new_castling_rights, board = move_piece.make_move(board, move, last_move.c_rights)
                    move.c_rights = new_castling_rights
                    rating = best_move(new_board_state, not turn, depth-1, alpha, beta, move)[0]
                    move.eval = rating
                    if beta > move.eval:
                        beta = move.eval
                        best = move
                    if alpha >= beta:
                        return beta, best
                return beta, best

#This is what is called by the main file process the request for the best move
def find_move(board, turn, difficulty=0, castling_rights=[True,True,True,True], last_move=("p",0,0)):
    #A move object is created out of the last move
    l_piece = board_conversions.piece_to_num[last_move[0]]
    l_move = move_generator.moves(l_piece,last_move[1], last_move[2])
    l_move.c_rights = castling_rights.copy()
    #The board is saved differently by the bot and the main code, so this converts it to the right type
    test_board = board_conversions.letters_to_num(board)
    #This calculates how deep the program should calculate based on the number of pieces on the board and the difficulty
    count = 0
    for item in test_board:
        if item != 0:
            count += 1
    d_max = difficulty + 3 + (5-int(math.sqrt(count)))
    d = 3
    t_start = time.time()
    #this runs the best move at deeper depths until either the best depth is reached, or you attempt a new depth after 1 seconds have passed
    while d_max >= d and time.time()-t_start < 1:
        eval, move = best_move(test_board, turn, d, -20000, 20000, l_move)
        d += 1
    print(time.time()-t_start)
    print(eval,d)
    return move

"""t = time.time()
eval, move = best_move(b,False,5,-200,200,[True,True,True,True],(0,0,0))
new = time.time()
print("Time Taken: " + str(new-t))
board_conversions.generate_test_board(b)
print(eval)
print(vars(move))
(new_board, move, castling_rights, old_board) = move_piece.make_move(b, move, [True,True,True,True])
board_conversions.generate_test_board(new_board)
print(eval)
print(vars(move))"""

"""board_conversions.generate_test_board(board_conversions.let_to_num(b))
move = (find_move(b, True))
print(vars(move))"""