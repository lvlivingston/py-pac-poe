# As a player (AAP), I want to see a welcome message at the start

----------------------
Let's play Py-Pac-Poe!
----------------------

# AAP, before being prompted for a move, I want to see the board printed out in the console, so that I know what moves have been made:

    A   B   C

1)  X |   | O 
    -----------
2)    | X |  
    -----------
3)  X | O | O 

# AAP, I want to be prompted with which player’s move it is.

Player X's Move

# AAP, I want to be prompted on how to enter a valid move so that I don’t make mistakes:

    A   B   C

1)  X |   | O 
    -----------
2)    | X |  
    -----------
3)  X | O | O 

Player X's Move (example B2):  

# AAP, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B or c/C) to make it easier to enter my move.

.lower()

# AAP, if I enter a move in an invalid format, or if I try to occupy a cell already taken, I want to see a message chastising me and be re-prompted:

Player X's Move (example B2): Z9
Bogus move! Try again...

Player X's Move (example B2):

# AAP, at the end of a game I want to see who won the game:

Player X wins the game! or It's a tie!