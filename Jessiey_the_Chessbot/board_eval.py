#Piece type chart
# 1 - pawn , 2 - knight , 3 - king , 4 - rook , 5 - bishop , 6 - queen. +8 if black
#True for white, False for black
#board state is a list of 64 numbers where each is a number (0 for empty)
#Last move is touple of len 3 with (piece type, moved from, moved to)

#- means black is winning

if __name__ == "__main__":
    import move_generator
else:
    from Jessiey_the_Chessbot import move_generator

#theses charts represent the eval of a specfic piece based on where it is one the board
#Uses mid game chart until the number of pieces is less than 16 and then starts using end game
mid_game_charts = ( #PAWN MG
100,  100,  100,  100,  100,  100,  100,  100,
176,  214,  147,  194,  189,  214,  132,   77,
82,   88,  106,  113,  150,  146,  110,   73,
67,   93,   83,   95,   97,   92,   99,   63,
55,   74,   80,   89,   94,   86,   90,   55,
55,   70,   68,   69,   76,   81,  101,   66,
52,   84,   66,   60,   69,   99,  117,   60,
100,  100,  100,  100,  100,  100,  100,  100,
#KNIGHT MG
116,  228,  271,  270,  338,  213,  278,  191,
225,  247,  353,  331,  321,  360,  300,  281,
258,  354,  343,  362,  389,  428,  375,  347,
300,  332,  325,  360,  349,  379,  339,  333,
298,  322,  325,  321,  337,  332,  332,  303,
287,  297,  316,  319,  327,  320,  327,  294,
276,  259,  300,  304,  308,  322,  296,  292,
208,  290,  257,  274,  296,  284,  293,  284,
#King MG
-11,   70,   55,   31,  -37,  -16,   22,   22,
37,   24,   25,   36,   16,    8,  -12,  -31,
33,   26,   42,   11,   11,   40,   35,   -2,
0,   -9,    1,  -21,  -20,  -22,  -15,  -60,
-25,   16,  -27,  -67,  -81,  -58,  -40,  -62,
7,   -2,  -37,  -77,  -79,  -60,  -23,  -26,
12,   15,  -13,  -72,  -56,  -28,   15,   17,
-6,   44,   29,  -58,    8,  -25,   34,   28,
#ROOK MG
493,  511,  487,  515,  514,  483,  485,  495,
493,  498,  529,  534,  546,  544,  483,  508,
465,  490,  499,  497,  483,  519,  531,  480,
448,  464,  476,  495,  484,  506,  467,  455,
442,  451,  468,  470,  476,  472,  498,  454,
441,  461,  468,  465,  478,  481,  478,  452,
443,  472,  467,  476,  483,  500,  487,  423,
459,  463,  470,  479,  480,  480,  446,  458,
#Bishop MG
292,  338,  254,  283,  299,  294,  337,  323,
316,  342,  319,  319,  360,  385,  343,  295,
342,  377,  373,  374,  368,  392,  385,  363,
332,  338,  356,  384,  370,  380,  337,  341,
327,  354,  353,  366,  373,  346,  345,  341,
335,  350,  351,  347,  352,  361,  350,  344,
333,  354,  354,  339,  344,  353,  367,  333,
309,  341,  342,  325,  334,  332,  302,  313,
#Queen MG
865,  902,  922,  911,  964,  948,  933,  928,
886,  865,  903,  921,  888,  951,  923,  940,
902,  901,  907,  919,  936,  978,  965,  966,
881,  885,  897,  894,  898,  929,  906,  915,
907,  884,  899,  896,  904,  906,  912,  911,
895,  916,  900,  902,  904,  912,  924,  917,
874,  899,  918,  908,  915,  924,  911,  906,
906,  899,  906,  918,  898,  890,  878,  858)

end_game_charts = (#PAWN EG
100,  100,  100,  100,  100,  100,  100,  100,
277,  270,  252,  229,  240,  233,  264,  285,
190,  197,  182,  168,  155,  150,  180,  181,
128,  117,  108,  102,   93,  100,  110,  110,
107,  101,   89,   85,   86,   83,   92,   91,
96,   96,   85,   92,   88,   83,   85,   82,
107,   99,   97,   97,  100,   89,   89,   84,
100,  100,  100,  100,  100,  100,  100,  100,
#KNIGHT EG
229,  236,  269,  250,  257,  249,  219,  188,
252,  274,  263,  281,  273,  258,  260,  229,
253,  264,  290,  289,  278,  275,  263,  243,
267,  280,  299,  301,  299,  293,  285,  264,
263,  273,  293,  301,  296,  293,  284,  261,
258,  276,  278,  290,  287,  274,  260,  255,
241,  259,  270,  277,  276,  262,  260,  237,
253,  233,  258,  264,  261,  260,  234,  215,
#KING EG
-74,  -43,  -23,  -25,  -11,   10,    1,  -12,
-18,    6,    4,    9,    7,   26,   14,    8,
-3,    6,   10,    6,    8,   24,   27,    3,
-16,    8,   13,   20,   14,   19,   10,   -3,
-25,  -14,   13,   20,   24,   15,    1,  -15,
-27,  -10,    9,   20,   23,   14,    2,  -12,
-32,  -17,    4,   14,   15,    5,  -10,  -22,
-55,  -40,  -23,   -6,  -20,   -8,  -28,  -47,
#ROOK EG
506,  500,  508,  502,  504,  507,  505,  503,
505,  506,  502,  502,  491,  497,  506,  501,
504,  503,  499,  500,  500,  495,  496,  496,
503,  502,  510,  500,  502,  504,  500,  505,
505,  509,  509,  506,  504,  503,  496,  495,
500,  503,  500,  505,  498,  498,  499,  489,
496,  495,  502,  505,  498,  498,  491,  499,
492,  497,  498,  496,  493,  493,  497,  480,
#BISHOP EG
288,  278,  287,  292,  293,  290,  287,  277,
289,  294,  301,  288,  296,  289,  294,  281,
292,  289,  296,  292,  296,  300,  296,  293,
293,  302,  305,  305,  306,  302,  296,  297,
289,  293,  304,  308,  298,  301,  291,  288,
285,  294,  304,  303,  306,  294,  290,  280,
285,  284,  291,  299,  300,  290,  284,  271,
277,  292,  286,  295,  294,  288,  290,  285,
#QUEEN EG
918,  937,  943,  945,  934,  926,  924,  942,
907,  945,  946,  951,  982,  933,  928,  912,
896,  921,  926,  967,  963,  937,  924,  915,
926,  944,  939,  962,  983,  957,  981,  950,
893,  949,  942,  970,  952,  956,  953,  936,
911,  892,  933,  928,  934,  942,  934,  924,
907,  898,  883,  903,  903,  893,  886,  888,
886,  887,  890,  872,  916,  890,  906,  879
)

#gets the evaluation of a specific piece
def eval_piece(piece,loc,mid_game=True):
    if mid_game:
        if piece < 8:
            return mid_game_charts[(piece-1)*64+loc]
        else:
            b_loc = 8*(7 - (loc//8)) + loc%8
            return -mid_game_charts[(piece-9)*64+b_loc]
    else:
        if piece < 8:
            return end_game_charts[(piece-1)*64+loc]
        else:
            b_loc = 8*(7 - (loc//8)) + loc%8
            return -end_game_charts[(piece-9)*64+b_loc]

#gets the evaluation of an entire board state
def eval(board_state, turn, last_move, castling_rights):
    count = 0
    for item in board_state:
        if item != 0:
            count += 1
    #uses number of pieces to decide whether to use midgame or end game chart(midgame chart is used for early game)
    if count <= 16:
        mid_game = False
    else:
        mid_game = True
    board_eval = 0
    #If you can't move, you are either in checkmate or stalemate, so this evaluates accordingly
    moves = move_generator.generate_moves(board_state, turn, last_move, castling_rights)
    if len(moves) == 0:
        if move_generator.check(board_state, turn, last_move, castling_rights):
            if turn:
                return -20000
            else:
                return 20000
        else:
            return 0
    king = 1
    #gets eval of each piece
    for index, piece in enumerate(board_state):
        if piece != 0:
            if piece == 3:
                king += 1
            elif piece == 11:
                king -= 1
            board_eval += eval_piece(piece,index,mid_game)
    #If a player is missing a king, the other wins
    if king == 2:
        return 20000
    if king == 0:
        return -20000
    return board_eval