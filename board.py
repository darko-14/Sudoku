board = ["-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-"]

dictionary = {
    11: board[0], 12: board[1], 13: board[2], 14: board[3], 15: board[4], 16: board[5], 17: board[6], 18: board[7], 19: board[8],
    21: board[9], 22: board[10], 23: board[11], 24: board[12], 25: board[13], 26: board[14], 27: board[15], 28: board[16], 29: board[17],
    31: board[18], 32: board[19], 33: board[20], 34: board[21], 35: board[22], 36: board[23], 37: board[24], 38: board[25], 39: board[26],
    41: board[27], 42: board[28], 43: board[29], 44: board[30], 45: board[31], 46: board[32], 47: board[33], 48: board[34], 49: board[35],
    51: board[36], 52: board[37], 53: board[38], 54: board[39], 55: board[40], 56: board[41], 57: board[42], 58: board[43], 59: board[44],
    61: board[45], 62: board[46], 63: board[47], 64: board[48], 65: board[49], 66: board[50], 67: board[51], 68: board[52], 69: board[53],
    71: board[54], 72: board[55], 73: board[56], 74: board[57], 75: board[58], 76: board[59], 77: board[60], 78: board[61], 79: board[62],
    81: board[63], 82: board[64], 83: board[65], 84: board[66], 85: board[67], 86: board[68], 87: board[69], 88: board[70], 89: board[71],
    91: board[72], 92: board[73], 93: board[74], 94: board[75], 95: board[76], 96: board[77], 97: board[78], 98: board[79], 99: board[80]
}


def displayBoard():
    print()
    print("   ╔═══════════╦═══════════╦═══════════╗")
    print(" 1 ║", board[0], "|", board[1], "|", board[2], "║", board[3], "|", board[4], "|", board[5], "║", board[6], "|", board[7], "|", board[8], "║") 
    print(" 2 ║", board[9], "|", board[10], "|", board[11], "║", board[12], "|", board[13], "|", board[14], "║", board[15], "|", board[16], "|", board[17], "║")
    print(" 3 ║", board[18], "|", board[19], "|", board[20], "║", board[21], "|", board[22], "|", board[23], "║", board[24], "|", board[25], "|", board[26], "║")
    print("   ╠═══════════╬═══════════╬═══════════╣")
    print(" 4 ║", board[27], "|", board[28], "|", board[29], "║", board[30], "|", board[31], "|", board[32], "║", board[33], "|", board[34], "|", board[35], "║")
    print(" 5 ║", board[36], "|", board[37], "|", board[38], "║", board[39], "|", board[40], "|", board[41], "║", board[42], "|", board[43], "|", board[44], "║")
    print(" 6 ║", board[45], "|", board[46], "|", board[47], "║", board[48], "|", board[49], "|", board[50], "║", board[51], "|", board[52], "|", board[53], "║")
    print("   ╠═══════════╬═══════════╬═══════════╣")
    print(" 7 ║", board[54], "|", board[55], "|", board[56], "║", board[57], "|", board[58], "|", board[59], "║", board[60], "|", board[61], "|", board[62], "║")
    print(" 8 ║", board[63], "|", board[64], "|", board[65], "║", board[66], "|", board[67], "|", board[68], "║", board[69], "|", board[70], "|", board[71], "║")
    print(" 9 ║", board[72], "|", board[73], "|", board[74], "║", board[75], "|", board[76], "|", board[77], "║", board[78], "|", board[79], "|", board[80], "║")
    print("   ╚═══════════╩═══════════╩═══════════╝")
    print("    ", "1  ", "2  ", "3  ", "4  ", "5  ", "6  ", "7  ", "8  ", "9  " )
    print()


displayBoard()

valid = True

while valid:

    keys = dictionary.keys()  # gets all the keys from dicitonary to a list
    values = dictionary.values()    # gets all the values from dicitonary to a list

    number = input("Enter number from 1-9: ")    
    number = int(number)

    allowedNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    if number in allowedNumbers:
        number = number
    else:
        print("Enter number from 1-9: ")
        valid = False

    position = input("Choose position by grid: ")
    position = int(position)


    if position in keys:
        dictionary[position] = number
        board[position] = number
        displayBoard()
    else:
        print("This ain't it chief!")
