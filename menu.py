import pygame
import re
import indicies_coordinate
#dictionary for calling assets
assets = {
    'title' : "chess_assets/Info/title.png",
    'settings' : "chess_assets/Info/settings.png",
    'variations' : "chess_assets/Info/variationsTitle.png",
    'botButton' : "chess_assets/Buttons/MainMenu/botButton.png",
    'botGrey' : "chess_assets/Buttons/MainMenu/botButtonGrey.png",
    'botRed' : "chess_assets/Buttons/MainMenu/botButtonRed.png",
    'coopButton' : "chess_assets/Buttons/MainMenu/coopButton.png",
    'coopGrey' : "chess_assets/Buttons/MainMenu/coopButtonGrey.png",
    'coopRed' : "chess_assets/Buttons/MainMenu/coopButtonRed.png",
    'variationsButton' : "chess_assets/Buttons/Variations/variationsButton.png",
    'variationsGrey' : "chess_assets/Buttons/Variations/variationsButtonGrey.png",
    'variationsRed' : "chess_assets/Buttons/Variations/variationsButtonRed.png",
    'backButton' : "chess_assets/Buttons/Settings/backButton.png",
    'backGrey' : "chess_assets/Buttons/Settings/backButtonGrey.png",
    'backRed' : "chess_assets/Buttons/Settings/backButtonRed.png",
    'blackWhiteOff' : "chess_assets/Buttons/Settings/blackWhiteButtonOff.png",
    'blackWhiteOffGrey' : "chess_assets/Buttons/Settings/blackWhiteButtonOffGrey.png",
    'blackWhiteOffRed' : "chess_assets/Buttons/Settings/blackWhiteButtonOffRed.png",
    'blackWhiteOn' : "chess_assets/Buttons/Settings/blackWhiteButtonOn.png",
    'blackWhiteOnGrey' : "chess_assets/Buttons/Settings/blackWhiteButtonOnGrey.png",
    'blackWhiteOnRed' : "chess_assets/Buttons/Settings/blackWhiteButtonOnRed.png",
    'boardFlipOff' : "chess_assets/Buttons/Settings/boardFlipButtonOff.png",
    'boardFlipOffGrey' : "chess_assets/Buttons/Settings/boardFlipButtonOffGrey.png",
    'boardFlipOffRed' : "chess_assets/Buttons/Settings/boardFlipButtonOffRed.png",
    'boardFlipOn' : "chess_assets/Buttons/Settings/boardFlipButtonOn.png",
    'boardFlipOnGrey' : "chess_assets/Buttons/Settings/boardFlipButtonOnGrey.png",
    'boardFlipOnRed' : "chess_assets/Buttons/Settings/boardFlipButtonOnRed.png",
    'redLinesOff' : "chess_assets/Buttons/Settings/redLinesButtonOff.png",
    'redLinesOffGrey' : "chess_assets/Buttons/Settings/redLinesButtonOffGrey.png",
    'redLinesOffRed' : "chess_assets/Buttons/Settings/redLinesButtonOffRed.png",
    'redLinesOn' : "chess_assets/Buttons/Settings/redLinesButtonOn.png",
    'redLinesOnGrey' : "chess_assets/Buttons/Settings/redLinesButtonOnGrey.png",
    'redLinesOnRed' : "chess_assets/Buttons/Settings/redLinesButtonOnRed.png",
    'redSpaceOff' : "chess_assets/Buttons/Settings/redSpaceButtonOff.png",
    'redSpaceOffGrey' : "chess_assets/Buttons/Settings/redSpaceButtonOffGrey.png",
    'redSpaceOffRed' : "chess_assets/Buttons/Settings/redSpaceButtonOffRed.png",
    'redSpaceOn' : "chess_assets/Buttons/Settings/redSpaceButtonOn.png",
    'redSpaceOnGrey' : "chess_assets/Buttons/Settings/redSpaceButtonOnGrey.png",
    'redSpaceOnRed' : "chess_assets/Buttons/Settings/redSpaceButtonOnRed.png",
    'settingsIcon' : "chess_assets/Buttons/Settings/settingsButtonIcon.png",
    'settingsIconGrey' : "chess_assets/Buttons/Settings/settingsButtonIconGrey.png",
    'settingsIconRed' : "chess_assets/Buttons/Settings/settingsButtonIconRed.png",
    'bestMove' : "chess_assets/Buttons/GameScreen/getBestMove.png",
    'bestMoveGrey' : "chess_assets/Buttons/GameScreen/getBestMoveGrey.png",
    'bestMoveRed' : "chess_assets/Buttons/GameScreen/getBestMoveRed.png",
    'offerDraw' : "chess_assets/Buttons/GameScreen/offferDraw.png",
    'offerDrawGrey' : "chess_assets/Buttons/GameScreen/offerDrawGrey.png",
    'offerDrawRed' : "chess_assets/Buttons/GameScreen/offerDrawRed.png",
    'dunsany' : "chess_assets/Buttons/Variations/dunsany.png",
    'dunsanyGrey' : "chess_assets/Buttons/Variations/dunsanyGrey.png",
    'dunsanyRed' : "chess_assets/Buttons/Variations/dunsanyRed.png",
    'swapColor' : "chess_assets/Buttons/Variations/swapColor.png",
    'swapColorGrey' : "chess_assets/Buttons/Variations/swapColorGrey.png",
    'swapColorRed' : "chess_assets/Buttons/Variations/swapColorRed.png",
    'brigade' : "chess_assets/Buttons/Variations/lightBrigade.png",
    'brigadeGrey' : "chess_assets/Buttons/Variations/lightBrigadeGrey.png",
    'brigadeRed' : "chess_assets/Buttons/Variations/lightBrigadeRed.png",
    'random' : "chess_assets/Buttons/Variations/random.png",
    'randomGrey' : "chess_assets/Buttons/Variations/randomGrey.png",
    'randomRed' : "chess_assets/Buttons/Variations/randomRed.png",
    'easy' : "chess_assets/Buttons/Settings/difficultyEasy.png",
    'easyGrey' : "chess_assets/Buttons/Settings/difficultyEasyGrey.png",
    'easyRed' : "chess_assets/Buttons/Settings/difficultyEasyRed.png",
    'medium' : "chess_assets/Buttons/Settings/difficultyMed.png",
    'mediumGrey' : "chess_assets/Buttons/Settings/difficultyMedGrey.png",
    'mediumRed' : "chess_assets/Buttons/Settings/difficultyMedRed.png",
    'hard' : "chess_assets/Buttons/Settings/difficultyHard.png",
    'hardGrey' : "chess_assets/Buttons/Settings/difficultHardGrey.png",
    'hardRed' : "chess_assets/Buttons/Settings/difficultyHardRed.png",
    'variantLabel' : "chess_assets/Info/variantLabel.png"
}

#function for getting the coordinate that will place an image in the center of a screen
def get_center(screen, img):
    return screen.get_width()/2 - img.get_width()/2
#function for if a mouse is over a button
def mouseOnButton(screen, img, y, x = None):
    mouseX, mouseY = pygame.mouse.get_pos()
    button = pygame.image.load(img)
    if x == None:
        x = get_center(screen, button)
    if x < mouseX < (x + button.get_width()) and y < mouseY < (y + button.get_height()):
        return True
    return False
#function for creating and highlighing buttons
def button(screen, settings, imgTuple, y, x = None, offset = 5):
    img = imgTuple[0]
    red = imgTuple[1]
    grey = imgTuple[2]
    button = pygame.image.load(img)
    if x == None:
        x = get_center(screen, button)
    if mouseOnButton(screen, img, y, x):
        button = pygame.image.load(red if settings[2] else grey)
        printY = y - offset
        printX = x - offset
    else:
        button = pygame.image.load(img)
        printY = y
        printX = x
    screen.blit(button, (printX, printY))
#creating and maintaining toggleable buttons for settings menu
def toggleButton(screen, settings, status, onTuple, offTuple, y, x = None):
    if status:
        imgTuple = onTuple
    else:
        imgTuple = offTuple
    button(screen, settings, imgTuple, y, x)
#function for creating and maintaining the highlighting of the settings icon
def setting_icon(screen, settings):
    button(screen, settings, (assets["settingsIcon"], assets['settingsIconRed'], assets['settingsIconGrey']), 640, 1000, 2)
#function for creating and maintaining the highlighting of the back button
def back_button(screen, settings):
    button(screen, settings, (assets['backButton'], assets['backRed'], assets["backGrey"]), 640, 20, 3)
#create and update start_menu
def start_menu(screen, color, settings):
    screen.fill(color)
    #Creates the coop button and handles coop button highlighting
    button(screen, settings, (assets["coopButton"], assets["coopRed"], assets["coopGrey"]), 335)
    #creates the bot button and handles bot button highlighting
    button(screen, settings, (assets["botButton"], assets["botRed"], assets["botGrey"]), 410)
    #creates the variant button and handles variant button highlighting 
    button(screen, settings, (assets["variationsButton"], assets["variationsRed"], assets["variationsGrey"]), 485)
    #creates setting button
    setting_icon(screen, settings)
    #Creates the title
    titleImage = pygame.image.load(assets["title"])
    screen.blit(titleImage, (get_center(screen,titleImage), 200))
#create and update the setting menu
def settings_menu(screen, color, settings, swapColor, difficulty):
    screen.fill(color)
    
    #Creates the settings title
    titleImage = pygame.image.load(assets["settings"])
    screen.blit(titleImage, (get_center(screen, titleImage), 200))
    #Creates the back button
    back_button(screen, settings)
    #Creates the board flip button
    if not swapColor:
        boardFlipOn = (assets['boardFlipOn'], assets['boardFlipOnRed'], assets['boardFlipOnGrey'])
        boardFlipOff = (assets['boardFlipOff'], assets['boardFlipOffRed'], assets['boardFlipOffGrey'])
        toggleButton(screen, settings, settings[0], boardFlipOn, boardFlipOff, 335, 215)
    #Creates the blackWhite button
    blackWhiteOn = (assets['blackWhiteOn'], assets['blackWhiteOnRed'], assets['blackWhiteOnGrey'])
    blackWhiteOff = (assets['blackWhiteOff'], assets['blackWhiteOffRed'], assets['blackWhiteOffGrey'])
    toggleButton(screen, settings, settings[1], blackWhiteOn, blackWhiteOff, 410, 215)
    #Creates the redLines button
    redLinesOn = (assets['redLinesOn'], assets['redLinesOnRed'], assets['redLinesOnGrey'])
    redLinesOff = (assets['redLinesOff'], assets['redLinesOffRed'], assets['redLinesOffGrey'])
    toggleButton(screen, settings, settings[2], redLinesOn, redLinesOff, 335, 565)
    #Creates the redSpace button
    redSpaceOn = (assets['redSpaceOn'], assets['redSpaceOnRed'], assets['redSpaceOnGrey'])
    redSpaceOff = (assets['redSpaceOff'], assets['redSpaceOffRed'], assets['redSpaceOffGrey'])
    toggleButton(screen, settings, settings[3], redSpaceOn, redSpaceOff, 410, 565)
    #Creates the difficulty button
    if difficulty == 0:
        diffTuple = (assets['easy'], assets['easyRed'], assets['easyGrey'])
    elif difficulty == 1:
        diffTuple = (assets['medium'], assets['mediumRed'], assets['mediumGrey'])
    elif difficulty == 2:
        diffTuple = (assets['hard'], assets['hardRed'], assets['hardGrey'])
    button(screen, settings, diffTuple, 485)
#create and update the variation menu
def variation_menu(screen, color, settings):
    screen.fill(color)

    #Creates the settings title
    variantTitle = pygame.image.load(assets["variations"])
    screen.blit(variantTitle, (get_center(screen, variantTitle), 200))
    #Creates the back button
    back_button(screen, settings)
    #Dunsany's Chess variation button
    button(screen, settings, (assets['dunsany'], assets['dunsanyRed'], assets['dunsanyGrey']), 335, 50)
    #Charge of the Light Brigade Chess variation button
    button(screen, settings, (assets['brigade'], assets['brigadeRed'], assets['brigadeGrey']), 410, 50)
    #variant chess label
    label = pygame.image.load(assets['variantLabel'])
    screen.blit(label, (get_center(screen, label), 285))
    #Random board state Chess variation button
    button(screen, settings, (assets['random'], assets['randomRed'], assets['randomGrey']), 335, 730)
    #Swap color Chess variation button
    button(screen, settings, (assets['swapColor'], assets['swapColorRed'], assets['swapColorGrey']), 410, 730)

def promotion_white(screen):
    screen.blit(pygame.image.load("chess_assets/Pawn_Promotion/Promotion_White.png"), (830, 250))

def promotion_black(screen):
    screen.blit(pygame.image.load("chess_assets/Pawn_Promotion/Promotion_Black.png"), (830, 250))
