# Sudoku
Sudoku in terminal

- global variable is_game_on = True

- make the board as a dictionary

- while global variable is True:
  generate random numbers from 1-9 and put them in random positions(~25)
  and display as a initial board
  - display the board function
  
- input number on the board and specific position:
  check if number is from 1-9 and position is in the dictionary as a key

- check if position is valid:
  check rows, columns, box
  - if it is place number on board and displayBoard()
  - else print "You cant place there"

- game is over function:
  global variable is False
  print "Well done."
  
  - Maybe a timer function
