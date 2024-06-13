global last_move
last_move = ("",0,0)

import pygame
import indicies_coordinate
import move_filter
import check
from Jessiey_the_Chessbot import jessiey, move_generator, board_conversions, move_piece
import castling
import global_variables
import os 
from menu import assets
import fischer_var
import randomChess


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1080, 720))
bgcolor = "gray"
clock = pygame.time.Clock()
running = True
pygame.display.toggle_fullscreen

#turn True is white and False is black
turn = True
turnReset = True
moveCount = 0
pygame.font.init()
font = pygame.font.SysFont(None, 48)
title_font = pygame.font.SysFont(None, 72)

pygame.mixer.init()

current_dir = os.path.dirname(__file__)

# Sound  when game ends 
end_path = os.path.join(current_dir, "chess_assets", "sounds", "notify.mp3")
end_sound = pygame.mixer.Sound(end_path)
end_sound_played = False

# Sound when a game starts 
start_path = os.path.join(current_dir, "chess_assets", "sounds", "game-start.mp3")
start_sound = pygame.mixer.Sound(start_path)
start_sound_played = False

# Sound when a piece moves but doesn't capture 
moving_path = os.path.join(current_dir, "chess_assets", "sounds", "move-self.mp3")
move_sound = pygame.mixer.Sound(moving_path)

# Sound when a piece captures another  
capturing_path = os.path.join(current_dir, "chess_assets", "sounds", "capture.mp3")
capturing_sound = pygame.mixer.Sound(capturing_path)

#Used for variant handling
variant = False
dunsanyWin = False
swapColor = False
colorSwapped = False
brigadePromo = False

board_state = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', '', '', '', '', '', '',
               '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
               'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
reset_board = board_state
reset_variant = board_state

variation = 'normal' # Options (so far) for variations are 'normal' & 'blindfold' 

# USED TO ENABLE FISCHER CHESS(LINK TO VARIATIONS BUTTON)
#commented out to test standard chess features - Michael (sorry)
# board_state = fischer_var.fischer_var(board_state)

selected_square_ind = 0
game_state = 0
best_from_ind = -1
best_to_ind = -1
checkmate = 0 #0 means nobody is in checkmate, 1 means white wins, 2 means black wins, 3 means the game ends in a stalemate.
#tuple that stores variables for settings
#settings
boardFlip = False
blackWhite = True
redLines = True
redSpace = True
settings = [boardFlip, blackWhite, redLines, redSpace]
prevScreen = 0
difficulty_level = 1   
promo_pending = False 

import board
import menu

#creates initial board
menu.start_menu(screen, bgcolor, settings)
#board.create_board(screen)

mouse_x, mouse_y = (0,0)

while running:
    #Makes it so pressing the red x closes the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Main menu state handling
        if game_state == 0:
            #Checking for mouse clicks on specific buttons
            if event.type == pygame.MOUSEBUTTONUP:
                if menu.mouseOnButton(screen, assets['coopButton'], 335):
                    game_state = 1
                    variant = False
                elif menu.mouseOnButton(screen, assets['botButton'], 410):
                    game_state = 2
                    variant = False
                elif menu.mouseOnButton(screen, assets['settingsIcon'], 640, 1000):
                    game_state = 3
                    prevScreen = 0
                elif menu.mouseOnButton(screen, assets['variationsButton'], 485):
                    game_state = 4
                    prevScreen = 0
        if game_state == 1 or game_state == 2:
            if not promo_pending:
                if game_state == 1 or turn:
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_x , mouse_y = pygame.mouse.get_pos()
                        if menu.mouseOnButton(screen, assets['bestMove'], 175, 735):
                            #pressing best move button
                            castling_rights = [not(global_variables.white_king_moved or global_variables.white_rk_moved),not(global_variables.white_king_moved or global_variables.white_rq_moved),not(global_variables.black_king_moved or global_variables.black_rk_moved),not(global_variables.black_king_moved or global_variables.black_rq_moved)]
                            top_move = jessiey.find_move(board_state, turn, difficulty_level, castling_rights, last_move=("p",0,0))
                            best_from_ind = top_move.previous_loc
                            best_to_ind = top_move.final_loc
                            print(vars(top_move))
                        #checking for settings button pressed
                        if menu.mouseOnButton(screen, assets['settingsIcon'], 640, 1000):
                            game_state = 3
                            prevScreen = 1
                        if menu.mouseOnButton(screen, assets['offerDraw'], 643, 735):
                            checkmate = 3
                        if 30 < mouse_x < 670 and 30 < mouse_y < 670:
                            mouse_x_col, mouse_y_row = indicies_coordinate.pygame_coords_to_coords(mouse_x, mouse_y)
                            #print('x=', mouse_x_col)
                            #print('y=', mouse_y_row)
                            new_square_ind = indicies_coordinate.coords_to_ind((9 - mouse_x_col), (9 - mouse_y_row)) if colorSwapped else indicies_coordinate.coords_to_ind(mouse_x_col if turn else (9 - mouse_x_col), mouse_y_row if turn else (9 - mouse_y_row)) if settings[0] else indicies_coordinate.coords_to_ind(mouse_x_col, mouse_y_row)
                            
                            if move_filter.move_check(board_state, turn, selected_square_ind, new_square_ind,last_move):
                                test_state = board_state.copy()
                                test_state[new_square_ind] = test_state[selected_square_ind]
                                test_state[selected_square_ind] = ""
                                piece = (board_state[selected_square_ind])

                                print(f"Selected Square Ind: {board_state[selected_square_ind]}")
                                print(f"New Square Ind : {board_state[new_square_ind]}")
                                if board_state[new_square_ind] == '':
                                        if not check.in_check(board_state,turn):
                                            pygame.mixer.Sound.play(move_sound)
                                else:
                                    pygame.mixer.Sound.play(capturing_sound)
                                # White Kingside castling
                                # Modifies the board state to fit the standard rules of castling for white's position 
                                if castling.white_castling_valid(board_state, turn, selected_square_ind, new_square_ind) and (new_square_ind - selected_square_ind == 2):
                                    
                                    test_state[selected_square_ind], test_state[selected_square_ind+1],test_state[new_square_ind],test_state[new_square_ind+1] = '','R','K','',
                                    global_variables.white_king_moved,global_variables.white_rk_moved = True, True

                                # White QueenSide Castling
                                elif castling.white_castling_valid(board_state, turn, selected_square_ind, new_square_ind) and (new_square_ind - selected_square_ind) == -2:

                                    test_state[new_square_ind - 2], test_state[new_square_ind - 1],test_state[new_square_ind],test_state[selected_square_ind - 1],test_state[selected_square_ind]= \
                                        '','','K','R',''
                                    global_variables.white_king_moved,global_variables.white_rq_moved = True, True

                                # Modifies the board state to fit the standard rules of castling for black's position 
                                if castling.black_castling_valid(board_state, turn, selected_square_ind, new_square_ind) and (new_square_ind - selected_square_ind == 2):

                                    test_state[selected_square_ind], test_state[selected_square_ind + 1],test_state[new_square_ind],test_state[new_square_ind + 1] = \
                                        '','r','k',''
                                    global_variables.black_king_moved,global_variables.black_rk_moved = True,True

                                elif castling.black_castling_valid(board_state, turn, selected_square_ind, new_square_ind) and (new_square_ind - selected_square_ind) == -2:

                                    test_state[selected_square_ind],test_state[selected_square_ind - 1],test_state[selected_square_ind - 2],test_state[selected_square_ind - 3],test_state[selected_square_ind - 4] = '','r','k','',''
                                    global_variables.black_king_moved,global_variables.black_rq_moved = True,True

                                
                                print(mouse_x_col,new_square_ind%8 + 1)
                                if (piece == "p" or piece == "P") and (board_state[new_square_ind] == "") and (selected_square_ind%8 != new_square_ind%8 ):
                                    print("executing")
                                    test_state[last_move[2]] = ""
                                
                                if not check.in_check(test_state, turn):
                                    for i in range(56,64):
                                        if "p" == test_state[i]:
                                            promo_pending = True
                                    for i in range(0,8):
                                        if "P" == test_state[i]:
                                            promo_pending = True
                                    if selected_square_ind == 63 or new_square_ind == 63:
                                        global_variables.white_rk_moved = True
                                    elif selected_square_ind == 56 or new_square_ind == 56:
                                        global_variables.white_rq_moved = True
                                    elif selected_square_ind == 0 or new_square_ind == 0:
                                        global_variables.black_rq_moved = True
                                    elif selected_square_ind == 7 or new_square_ind == 7:
                                        global_variables.black_rk_moved = True

                                    if piece == "k":
                                        global_variables.black_king_moved = True
                                    elif piece == "K":
                                        global_variables.white_king_moved = True

                                    board_state = test_state
                                    turn = not turn
                                    #counts for swap color
                                    moveCount += 1
                                    #last_move is (piece that last moved, where it went from, where it went to)
                                    last_move = (piece,selected_square_ind,new_square_ind)
                                    print(last_move)
                                    #check for check mate
                                    castling_rights = [not(global_variables.white_king_moved or global_variables.white_rk_moved),not(global_variables.white_king_moved or global_variables.white_rq_moved),not(global_variables.black_king_moved or global_variables.black_rk_moved),not(global_variables.black_king_moved or global_variables.black_rq_moved)]
                                    l_piece = board_conversions.piece_to_num[last_move[0]]
                                    l_move = move_generator.moves(l_piece,last_move[1], last_move[2])
                                    l_move.c_rights = castling_rights
                                    if not promo_pending:
                                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                                    #handles swap color
                                    if moveCount % 10 == 0 and swapColor:
                                        for i, item in enumerate(board_state):
                                            if item.islower():
                                                board_state[i] = item.capitalize()
                                            if item.isupper():
                                                board_state[i] = item.lower()
                                        board_state.reverse()
                                        colorSwapped = not colorSwapped
                                        turn = not turn
                                    
                                

                            best_from_ind = -1
                            best_to_ind = -1
                            selected_square_ind = new_square_ind 
                            #print("checkmate: ", checkmate)



                    
        if game_state == 3:
            #Checking for mouse clicks on specific buttons
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                #Checking for back button
                #960, 640
                if menu.mouseOnButton(screen, assets['backButton'], 640, 20):
                    game_state = prevScreen
                #Checking for boardFlip button
                if menu.mouseOnButton(screen, assets['boardFlipOn'], 335, 215) and not swapColor:
                    settings[0] = not settings[0]
                #Checking for blackWhite button
                if menu.mouseOnButton(screen, assets['blackWhiteOn'], 410, 215):
                    settings[1] = not settings[1]
                #Checking for redLines button
                if menu.mouseOnButton(screen, assets['redLinesOn'], 335, 565):
                    settings[2] = not settings[2]
                #Checking for redSpace button
                if menu.mouseOnButton(screen, assets['redSpaceOn'], 410, 565):
                    settings[3] = not settings[3]
                #Checking for difficulty button
                if menu.mouseOnButton(screen, assets['easy'], 485):
                    if difficulty_level < 2:
                        difficulty_level += 1
                    else:
                        difficulty_level = 0
        if game_state == 4:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                #Checking for back button
                #960, 640
                if menu.mouseOnButton(screen, assets['backButton'], 640, 20):
                    game_state = prevScreen
                #handles variant menu dunsany chess button
                elif menu.mouseOnButton(screen, assets['dunsany'], 335, 50):
                    board_state = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 
                                   'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 
                                    '', '', '', '', '', '', '', '',
                                    '', '', '', '', '', '', '', '', 
                                    '', '', '', '', '', '', '', '', 
                                    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
                                    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
                                    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
                    reset_variant = board_state
                    dunsanyWin = True
                    turn = False
                    turnReset = False
                    variant = True
                    game_state = 1
                #handles variant menu swapColor chess
                elif menu.mouseOnButton(screen, assets['swapColor'], 410, 730):
                    swapColor = True
                    variant = True
                    game_state = 1
                #handles variant menu charge of the light brigade chess
                elif menu.mouseOnButton(screen, assets['brigade'], 410, 50):
                    board_state = ['n', 'n', 'n', 'n', 'k', 'n', 'n', 'n', 
                                   'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 
                                    '', '', '', '', '', '', '', '',
                                    '', '', '', '', '', '', '', '', 
                                    '', '', '', '', '', '', '', '', 
                                    '', '', '', '', '', '', '', '',
                                    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
                                    '', 'Q', '', 'Q', 'K', '', 'Q', '']
                    reset_variant = board_state
                    variant = True
                    brigadePromo = True
                    game_state = 1
                #handles variant menu random board_state chess
                elif menu.mouseOnButton(screen, assets['random'], 335, 730):
                    board_state = randomChess.randomBoard()
                    reset_variant = 'r'
                    variant = True
                    game_state = 1

    if game_state == 0:
        menu.start_menu(screen, bgcolor, settings)
    elif game_state == 1 or game_state == 2:
        # Add sound for capturing and moving  
        board.create_board(screen, settings)
        board.update_pieces(board_state, screen, turn, mouse_x, mouse_y,best_from_ind, best_to_ind, settings, colorSwapped,variation)
        menu.setting_icon(screen, settings)
        menu.button(screen, settings, (assets['offerDraw'], assets['offerDrawRed'], assets['offerDrawGrey']), 643, 735)
        if not start_sound_played:
            pygame.mixer.Sound.play(start_sound)
            start_sound_played = True
        
        
        game_mode = pygame.image.load("chess_assets/Info/coopIndicate.png") if game_state == 1 else pygame.image.load("chess_assets/Info/botIndicate.png") if game_state == 2 else None
        turn_indicator = pygame.image.load("chess_assets/Info/whiteIndicate.png") if turn else pygame.image.load("chess_assets/Info/blackIndicate.png")
    
        screen.blit(game_mode, (780, 40))
        screen.blit(turn_indicator, (780, 100))
        menu.button(screen, settings, (assets['bestMove'], assets['bestMoveRed'], assets['bestMoveGrey']), 175, 735)
        
        
        # This displays the winner and resets the required variables if the user wants to play again 
        if checkmate != 0 :
            
            board.display_winner(screen,checkmate)
            if not end_sound_played:
                pygame.mixer.Sound.play(end_sound)
                end_sound_played = True
            
            # If mouse is pressed on the location of the Play Again button, reset the appropriate variables 
            if 786 < mouse_x < 983 and 352 < mouse_y < 401 and event.type == pygame.MOUSEBUTTONUP:
                checkmate = 0             
                if variant:
                    board_state = randomChess.randomBoard() if reset_variant == 'r' else reset_variant
                else:
                    board_state = reset_board
                turn = turnReset
                end_sound_played = False
                start_sound_played = False
                
                # If the user wants to go back to the main menu, reset the variables in case he wants to play another game  
            elif 785 < mouse_x < 985 and 422 < mouse_y < 465 and event.type == pygame.MOUSEBUTTONUP:
                checkmate = 0 
                game_state = 0 
                turn = turnReset
                board_state = reset_board
                end_sound_played = False
                start_sound_played = False 
                variant = False
                dunsanyWin = False
                swapColor = False
                colorSwapped = False
                brigadePromo = False

                
                menu.start_menu(screen, bgcolor, settings)
        if game_state == 2 and not turn:
            castling_rights = [not(global_variables.white_king_moved or global_variables.white_rk_moved),not(global_variables.white_king_moved or global_variables.white_rq_moved),not(global_variables.black_king_moved or global_variables.black_rk_moved),not(global_variables.black_king_moved or global_variables.black_rq_moved)]
            top_move = jessiey.find_move(board_state, turn, difficulty_level, castling_rights, last_move=("p",0,0))
            best_from_ind = top_move.previous_loc
            best_to_ind = top_move.final_loc
            
            print(vars(top_move))
            piece_moved = board_conversions.num_to_p[top_move.piece]
            moveable_board = board_conversions.letters_to_num(board_state)
            (new_board, move, new_castling_rights, old_board) = move_piece.make_move(moveable_board, top_move, castling_rights)
            board_state = board_conversions.nums_to_lets(new_board)
            l_move = top_move
            last_move = [piece_moved,best_from_ind,best_to_ind]

            if not new_castling_rights[0]:
                global_variables.white_rk_moved = True
                global_variables.white_king_moved = True
            elif not new_castling_rights[1]:
                global_variables.white_rq_moved = True
                global_variables.white_king_moved = True
            elif not new_castling_rights[2]:
                global_variables.black_rk_moved = True
                global_variables.black_king_moved = True
            elif not new_castling_rights[3]:
                global_variables.black_rq_moved = True
                global_variables.black_king_moved = True

            turn = not turn
        
    elif game_state == 3:
        menu.settings_menu(screen, bgcolor, settings, swapColor, difficulty_level)
    #make variations menu
    elif game_state == 4:
        menu.variation_menu(screen, bgcolor, settings)
    #handle white loss for Dunsany chess
    if dunsanyWin:
        if 'P' not in board_state:
            checkmate = 2


    if promo_pending:
        for i in range(56,64):
            if "p" == board_state[i]:
                menu.promotion_black(screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x , mouse_y = pygame.mouse.get_pos()
                    if 830 < mouse_x < 910 and 250 < mouse_y < 330 and not brigadePromo:
                        board_state[i] = "q"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
                    elif 830 < mouse_x < 910 and 340 < mouse_y < 420 and not brigadePromo:
                        board_state[i] = "r"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
                    elif 830 < mouse_x < 910 and 430 < mouse_y < 510 and not brigadePromo:
                        board_state[i] = "b"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
                    elif 830 < mouse_x < 910 and 520 < mouse_y < 600:
                        board_state[i] = "n"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
        for i in range(0,8):
            if "P" == board_state[i]:
                menu.promotion_white(screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x , mouse_y = pygame.mouse.get_pos()
                    if 830 < mouse_x < 910 and 250 < mouse_y < 330:
                        board_state[i] = "Q"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
                    elif 830 < mouse_x < 910 and 330 < mouse_y < 410 and not brigadePromo:
                        board_state[i] = "R"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
                    elif 830 < mouse_x < 910 and 430 < mouse_y < 510 and not brigadePromo:
                        board_state[i] = "B"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
                    elif 830 < mouse_x < 910 and 520 < mouse_y < 600 and not brigadePromo:
                        board_state[i] = "N"
                        checkmateable_boardstate = board_conversions.letters_to_num(board_state)
                        checkmate = move_generator.checkmate(checkmateable_boardstate,turn,l_move)
                        promo_pending = False
    

    # puts display onto screen
    pygame.display.flip()

    clock.tick(30)  # Sets FPS to 60

pygame.quit()