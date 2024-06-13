import pygame
import indicies_coordinate
import menu


image_size = (70,70)

piece_imgs = {
        "P" : pygame.image.load("chess_assets/Tournament_Pieces/wp.png"),
        "N" : pygame.image.load("chess_assets/Tournament_Pieces/wn.png"),
        "R" : pygame.image.load("chess_assets/Tournament_Pieces/wr.png"),
        "B" : pygame.image.load("chess_assets/Tournament_Pieces/wb.png"),
        "K" : pygame.image.load("chess_assets/Tournament_Pieces/wk.png"),
        "Q" : pygame.image.load("chess_assets/Tournament_Pieces/wq.png"),
        "p" : pygame.image.load("chess_assets/Tournament_Pieces/bp.png"),
        "n" : pygame.image.load("chess_assets/Tournament_Pieces/bn.png"),
        "r" : pygame.image.load("chess_assets/Tournament_Pieces/br.png"),
        "b" : pygame.image.load("chess_assets/Tournament_Pieces/bb.png"),
        "k" : pygame.image.load("chess_assets/Tournament_Pieces/bk.png"),
        "q" : pygame.image.load("chess_assets/Tournament_Pieces/bq.png")
    }

def create_board(screen, settings):
    screen.fill("white")
    #Screen size is (1280, 720)
    #Board size is (640, 640) and centered at (350, 350)
    #Top right of board is (30,30)
    pygame.draw.rect(screen, "red" if settings[2] else (113, 113, 113), pygame.Rect(20, 20, 660, 660))
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                pygame.draw.rect(screen, pygame.Color(255, 255, 255) if settings[1] else pygame.Color(233, 236, 208), pygame.Rect(30+80*i, 30+80*j, 80, 80))
            else:
                pygame.draw.rect(screen, pygame.Color(30, 30, 30) if settings[1] else pygame.Color(113, 150, 86), pygame.Rect(30+80*i, 30+80*j, 80, 80))

def update_pieces(board_state, screen, turn, mouse_x, mouse_y, from_ind, to_ind, settings, colorSwapped,variation):
    selected_x , selected_y = (((mouse_x-30)//80)*80+30,((mouse_y-30)//80)*80+30)
    if settings[3] and 20 < selected_x < 670 and 20 < selected_y < 670:
        pygame.draw.rect(screen, "red", pygame.Rect(selected_x, selected_y, 80, 80))
    if from_ind != -1:
        from_x, from_y = indicies_coordinate.ind_to_coords(from_ind if turn or not settings[0] else (63-from_ind))
        to_x, to_y = indicies_coordinate.ind_to_coords(to_ind if turn or not settings[0] else (63-to_ind))
        if turn:
            pygame.draw.rect(screen, "yellow", pygame.Rect(-50+80*from_x, -50+80*from_y, 80, 80))
            pygame.draw.rect(screen, "yellow", pygame.Rect(-50+80*to_x, -50+80*to_y, 80, 80))
        else:
            pygame.draw.rect(screen, "yellow", pygame.Rect(-50+80*from_x, -50+80*from_y, 80, 80))
            pygame.draw.rect(screen, "yellow", pygame.Rect(-50+80*to_x, -50+80*to_y, 80, 80))
    for index, item in enumerate(board_state[::-1] if colorSwapped else (board_state if turn else board_state[::-1]) if settings[0] else board_state):
        if item != '':
            item_x , item_y = indicies_coordinate.ind_to_coords(index)
            if variation == 'blindfold':
                continue
                
            elif variation == 'normal':
                img = pygame.transform.scale(piece_imgs[item], image_size)
                screen.blit(img, (-50+80.5*item_x, -50+80.5*item_y))
    #create settings button
    screen.blit(pygame.image.load("chess_assets/Buttons/Settings/settingsButtonIcon.png"), (1000, 640))


def display_winner(screen,checkmate):

    messages = {
        1: pygame.image.load("chess_assets/Info/white_wins1.png"),
        2: pygame.image.load("chess_assets/Info/black_wins1.png"),
        3: pygame.image.load("chess_assets/Info/draw.png") 
    }
    
    # Load the appropriate win message   
    winner_image = messages[checkmate]
    winner_image = pygame.transform.scale(winner_image,(170,40))
    screen.blit(winner_image,(805,300))
    
    # Load the play again and menu buttons  
    play_again_image = pygame.image.load("chess_assets/Info/play_again.png")
    main_menu_button = pygame.image.load("chess_assets/Info/Main_Menu.png")
    
    play_again_image = pygame.transform.scale(play_again_image,(200,53))
    main_menu_button = pygame.transform.scale(main_menu_button,(200,45))
    screen.blit(play_again_image,(785,350))
    screen.blit(main_menu_button,(785,420))
        