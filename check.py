import re

#Turn refers to turn of player being tested as in check(True is checking white king. False is checking black king.)
#See video for inspiration on how code works: https://www.youtube.com/watch?v=fhNc0q5N3p0

def in_check(board_state, turn):
    #Creates new board with padding of 7 hashtags on the left
    check_board = ""
    new_board = ""
    for item in board_state:
        if item == "":
            new_board += " "
        else:
            new_board += item
    for i in range(8):
        check_board = check_board + new_board[8*i:8*i+8] + "0000000"
    #Checks if any piece can threaten the king using regex
    if turn:
        pawn_threat = re.search("p.{13}K|p.{15}K",check_board)
        horizontal_vertical_threat = re.search("[rq]\s*K|K\s*[rq]|[rq].{14}(\s.{14})*K|K.{14}(\s.{14})*[rq]",check_board)
        diagonal_threat = re.search("[bq].{13}(\s.{13})*K|[bq].{15}(\s.{15})*K|K.{13}(\s.{13})*[bq]|K.{15}(\s.{15})*[bq]",check_board)
        knight_threat = re.search("n(.){30}K|n(.){28}K|n(.){16}K|n(.){12}K|K(.){30}n|K(.){28}n|K(.){16}n|K(.){12}n",check_board)
    else:
        pawn_threat = re.search("k.{13}P|k.{15}P",check_board)
        horizontal_vertical_threat = re.search("[RQ]\s*k|k\s*[RQ]|[RQ].{14}(\s.{14})*k|k.{14}(\s.{14})*[RQ]",check_board)
        diagonal_threat = re.search("[BQ].{13}(\s.{13})*k|[BQ].{15}(\s.{15})*k|k.{13}(\s.{13})*[BQ]|k.{15}(\s.{15})*[BQ]",check_board)
        knight_threat = re.search("N(.){30}k|N(.){28}k|N(.){16}k|N(.){12}k|k(.){30}N|k(.){28}N|k(.){16}N|k(.){12}N",check_board)
    king_threat = re.search("k.{13,15}K|kK|K.{13,15}k|Kk",check_board)
    if pawn_threat == None and horizontal_vertical_threat == None and diagonal_threat == None and knight_threat == None and king_threat == None:
        return False
    return True

