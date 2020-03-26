###########################################################################################################################
##                                                                                                                       ##
##                                                                                                                       ##             
##                ###########  ####     ####  ##########          #######       ####    ####  ####     ####              ## 
##                ###########  ####     ####  ############      ###########     ####   ####   ####     ####              ## 
##                ###          ####     ####  ####     ####    #####    #####   ####  ####    ####     ####              ##     
##                ###          ####     ####  ####      ####  ####        ####  #### ####     ####     ####              ## 
##                ###########  ####     ####  ####      ####  ####        ####  ########      ####     ####              ## 
##                ###########  ####     ####  ####      ####  ####        ####  ########      ####     ####              ## 
##                        ###  ####     ####  ####      ####  ####        ####  #### ####     ####     ####              ##      
##                        ###  #####   #####  ####     ####    #####    #####   ####  ####    #####   #####              ## 
##                ###########   ###########   ############      ###########     ####   ####    ###########               ## 
##                ###########     #######     ##########          #######       ####    ####     #######                 ##            
##                                                                                                                       ##
##                                                                                                                       ## 
###########################################################################################################################

board = {
    11: "-", 12: "-", 13: "-", 14: "-", 15: "-", 16: "-", 17: "-", 18: "-", 19: "-",
    21: "-", 22: "-", 23: "-", 24: "-", 25: "-", 26: "-", 27: "-", 28: "-", 29: "-",
    31: "-", 32: "-", 33: "-", 34: "-", 35: "-", 36: "-", 37: "-", 38: "-", 39: "-",
    41: "-", 42: "-", 43: "-", 44: "-", 45: "-", 46: "-", 47: "-", 48: "-", 49: "-",
    51: "-", 52: "-", 53: "-", 54: "-", 55: "-", 56: "-", 57: "-", 58: "-", 59: "-",
    61: "-", 62: "-", 63: "-", 64: "-", 65: "-", 66: "-", 67: "-", 68: "-", 69: "-",
    71: "-", 72: "-", 73: "-", 74: "-", 75: "-", 76: "-", 77: "-", 78: "-", 79: "-",
    81: "-", 82: "-", 83: "-", 84: "-", 85: "-", 86: "-", 87: "-", 88: "-", 89: "-",
    91: "-", 92: "-", 93: "-", 94: "-", 95: "-", 96: "-", 97: "-", 98: "-", 99: "-"
}

gameIsOn = True


def displayBoard():
    print()
    print("   ╔═══════════╦═══════════╦═══════════╗")
    print(" 1 ║", board[11], "|", board[12], "|", board[13], "║", board[14], "|", board[15], "|", board[16], "║", board[17], "|", board[18], "|", board[19], "║") 
    print(" 2 ║", board[21], "|", board[22], "|", board[23], "║", board[24], "|", board[25], "|", board[26], "║", board[27], "|", board[28], "|", board[29], "║")
    print(" 3 ║", board[31], "|", board[32], "|", board[33], "║", board[34], "|", board[35], "|", board[36], "║", board[37], "|", board[38], "|", board[39], "║")
    print("   ╠═══════════╬═══════════╬═══════════╣")
    print(" 4 ║", board[41], "|", board[42], "|", board[43], "║", board[44], "|", board[45], "|", board[46], "║", board[47], "|", board[48], "|", board[49], "║")
    print(" 5 ║", board[51], "|", board[52], "|", board[53], "║", board[54], "|", board[55], "|", board[56], "║", board[57], "|", board[58], "|", board[59], "║")
    print(" 6 ║", board[61], "|", board[62], "|", board[63], "║", board[64], "|", board[65], "|", board[66], "║", board[67], "|", board[68], "|", board[69], "║")
    print("   ╠═══════════╬═══════════╬═══════════╣")
    print(" 7 ║", board[71], "|", board[72], "|", board[73], "║", board[74], "|", board[75], "|", board[76], "║", board[77], "|", board[78], "|", board[79], "║")
    print(" 8 ║", board[81], "|", board[82], "|", board[83], "║", board[84], "|", board[85], "|", board[86], "║", board[87], "|", board[88], "|", board[89], "║")
    print(" 9 ║", board[91], "|", board[92], "|", board[93], "║", board[94], "|", board[95], "|", board[96], "║", board[97], "|", board[98], "|", board[99], "║")
    print("   ╚═══════════╩═══════════╩═══════════╝")
    print("    ", "1  ", "2  ", "3  ", "4  ", "5  ", "6  ", "7  ", "8  ", "9  " )
    print()


def play_game():
    displayBoard()
    while gameIsOn:
        validNumbers = [1,2,3,4,5,6,7,8,9]
        number = input("Enter number from 1-9: ")    
        number = int(number)
        if number in validNumbers:

            position = input("Choose position by YX axis: ")
            position = int(position)


            if position in board.keys():
                if board[position] == "-":
                    board[position] = number
                    displayBoard()
                else:
                    print("That position is already filled.")
            else:
                print("No such number on the grid!")

        else:
            print("The number needs to be from 1 to 9!")


        # check_if_table_is_full()


def check_valid_position():
    check_row()
    check_column()
    check_box()

def check_row():
    row_1 = [ board.get(11), board.get(12), board.get(13), board.get(14), board.get(15), board.get(16), board.get(17), board.get(18).board.get(19) ]
    row_2 = [ board.get(21), board.get(22), board.get(23), board.get(24), board.get(25), board.get(26), board.get(27), board.get(28).board.get(29) ]
    row_3 = [ board.get(31), board.get(32), board.get(33), board.get(34), board.get(35), board.get(36), board.get(37), board.get(38).board.get(39) ]
    row_4 = [ board.get(41), board.get(42), board.get(43), board.get(44), board.get(45), board.get(46), board.get(47), board.get(48).board.get(49) ]
    row_5 = [ board.get(51), board.get(52), board.get(53), board.get(54), board.get(55), board.get(56), board.get(57), board.get(58).board.get(59) ]
    row_6 = [ board.get(61), board.get(62), board.get(63), board.get(64), board.get(65), board.get(66), board.get(67), board.get(68).board.get(69) ]
    row_7 = [ board.get(71), board.get(72), board.get(73), board.get(74), board.get(75), board.get(76), board.get(77), board.get(78).board.get(79) ]
    row_8 = [ board.get(81), board.get(82), board.get(83), board.get(84), board.get(85), board.get(86), board.get(87), board.get(88).board.get(89) ]
    row_9 = [ board.get(91), board.get(92), board.get(93), board.get(94), board.get(95), board.get(96), board.get(97), board.get(98).board.get(99) ]

    rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]

    for row in rows:
        if set(row):
            return True
        else:
            return False

            
def check_column():
    column_1 = [ board.get(11), board.get(21), board.get(31), board.get(41), board.get(51), board.get(61), board.get(71), board.get(81).board.get(91) ]
    column_2 = [ board.get(12), board.get(22), board.get(32), board.get(42), board.get(52), board.get(62), board.get(72), board.get(82).board.get(92) ]
    column_3 = [ board.get(13), board.get(23), board.get(33), board.get(43), board.get(53), board.get(63), board.get(73), board.get(83).board.get(93) ]
    column_4 = [ board.get(14), board.get(24), board.get(34), board.get(44), board.get(54), board.get(64), board.get(74), board.get(84).board.get(94) ]
    column_5 = [ board.get(15), board.get(25), board.get(35), board.get(45), board.get(55), board.get(65), board.get(75), board.get(85).board.get(95) ]
    column_6 = [ board.get(16), board.get(26), board.get(36), board.get(46), board.get(56), board.get(66), board.get(76), board.get(86).board.get(96) ]
    column_7 = [ board.get(17), board.get(27), board.get(37), board.get(47), board.get(57), board.get(67), board.get(77), board.get(87).board.get(97) ]
    column_8 = [ board.get(18), board.get(28), board.get(38), board.get(48), board.get(58), board.get(68), board.get(78), board.get(88).board.get(98) ]
    column_9 = [ board.get(19), board.get(29), board.get(39), board.get(49), board.get(59), board.get(69), board.get(79), board.get(89).board.get(99) ]

    columns = [column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8, column_9]

    for col in columns:
        if set(col):
            return True
        else:
            return False


def check_box():
    box_1 = [ board.get(11), board.get(12), board.get(13), board.get(21), board.get(22), board.get(23), board.get(31), board.get(32), board.get(33) ]
    box_2 = [ board.get(14), board.get(15), board.get(16), board.get(24), board.get(25), board.get(26), board.get(34), board.get(35), board.get(36) ]
    box_3 = [ board.get(17), board.get(18), board.get(19), board.get(27), board.get(28), board.get(29), board.get(37), board.get(38), board.get(39) ]
    box_4 = [ board.get(41), board.get(42), board.get(43), board.get(51), board.get(52), board.get(53), board.get(61), board.get(62), board.get(63) ]
    box_5 = [ board.get(44), board.get(45), board.get(46), board.get(54), board.get(55), board.get(56), board.get(64), board.get(65), board.get(66) ]
    box_6 = [ board.get(47), board.get(48), board.get(49), board.get(57), board.get(58), board.get(59), board.get(67), board.get(68), board.get(69) ]
    box_7 = [ board.get(71), board.get(72), board.get(73), board.get(81), board.get(82), board.get(83), board.get(91), board.get(92), board.get(93) ]
    box_8 = [ board.get(74), board.get(75), board.get(76), board.get(84), board.get(85), board.get(86), board.get(94), board.get(95), board.get(96) ]
    box_9 = [ board.get(77), board.get(78), board.get(79), board.get(87), board.get(88), board.get(89), board.get(97), board.get(98), board.get(99) ]

    boxes = [box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9]

    for box in boxes:
        if set(box):
            return True
        else:
            return False


def check_if_table_is_full():
    global gameIsOn
    for i in board.values():
        if i == "-":
            gameIsOn = True
        else:
            game_is_over()


def game_is_over():
    global gameIsOn
    check_valid_position()
    gameIsOn = False
    print("Well done!")


play_game()