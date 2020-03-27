# Sudoku
Sudoku in terminal

- global variable is_game_on = True                                                     # DONE

- make the board as a dictionary                                                        # DONE

- while global variable is True:                                                        # DONE
  generate random numbers from 1-9 and put them in random positions(~25)                # DONE
  and display as a initial board                                                        # DONE
  - ( generated numbers follow validation rules )                                       ?
  - display the board function                                                          # DONE
  
- input number on the board and specific position:                                      # DONE
  check if number is from 1-9 and position is in the dictionary as a key                # DONE

- function for not overriding a position                                                # DONE

- check if position is valid:                                                           # DONE
  check rows, columns, box                                                              # DONE  
  ( check if valid as a condition for the generating function and                       # DONE
    at the end to see if Win or Lose )
    ( dont deny the player to place number at any empty position )                      # DONE

- game is over function:                                                                # DONE
  global variable is False                                                              # DONE
  print "Well done."                                                                    # DONE   
   
- Backtracking algorithm for solving the game                                           ?    

  - Maybe a timer function                                                              #DONE      
