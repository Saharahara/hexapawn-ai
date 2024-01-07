# hexapawn-ai
Hexapawn-ai is a program that sets the user against an ai that begins to learn to play the game optimally. 

The game hexapawn, is a 2-player game that involves a 3*3 board and 6 pawns, 3 from each team placed on the first and last rows of the board. The movement of each piece is similar to that of pawns on a chessboard. A piece can either move forward one unit or attack the opponents pawn by moving forward by one unit diagonally. A player wins when it kills all opponent member pawns, brings it's pawn to the other side of the board or makes movement impossible for the opponent. 

Initially the game starts out with the user as the first person and the ai as the second person. The AI is not aware of the rules, and could try moving any of its pawns to any unit of the row right infront of it. Each time it learns that it's move was invalid it will never make that attempt again. After each game a database of all the states in a game, and the weightage of the movements to be made is stored. If the game was a failure for the ai, the weightage of each attempt made during the game will decrease, and if it wins the weightaeg of each jmove made will increase. When the game is played enough times, eventually the AI will begin to learn and play the game optimally, making it impossible for the user to win. Essentially the user teaches the AI how to play and win the game.

Inorder to play the game, clone and cd into the 'hexapawn-ai' repo and run it the matchbox.py file. 
```bash
  python3 matchbox.py

