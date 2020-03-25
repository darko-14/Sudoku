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


displayBoard()

while True:

    validNumbers = [1,2,3,4,5,6,7,8,9]
    number = input("Enter number from 1-9: ")    
    number = int(number)
    if number in validNumbers:

        print("Choose first a number from Y-axis, than a number from X-axis")
        position = input("Choose position by grid: ")
        position = int(position)


        if position in board.keys():
            board[position] = number
            displayBoard()
        else:
            print("This ain't it chief!")
    else:
        print("Wrong number!")


