# Tic Tac Toe AI Game Development

This is a game created on Python of the famous Tic Tac Toe game. The AI wins a considerable of times. The game is a bit monotonous i.e. the AI will make the same moves for same input given. 

This is the position of the game moves user can input:
- 0 &ensp;  1 &ensp;  2     &emsp; &emsp; &emsp; &emsp;     _  &ensp; _  &ensp; _ 
- 3 &ensp;  4 &ensp;  5     &emsp; &emsp; &emsp; &emsp;    _  &ensp; _  &ensp; _ 
- 6  &ensp; 7 &ensp;  8     &emsp;  &emsp; &emsp; &emsp;   _ &ensp;  _  &ensp; _

1. The game files implement the following algorithm. it is a very basic algorithm following a set of simple rules to make a move. This is the list of preferred order of moves taken by AI.
    - Wins immediately
    - Prevents an immediate loss
    - Places AI in 1 move away from a win
    - Prevents user from being a single move away from win.
    - First possible move from position 0 to position 8.
    The disadvantages are quite great. This AI is extremely weak towards variations. It plays the same moves any time and a certain set of strategies result in it losing

2. The minimax files implement the famous minimax algorithm. This algorithm relies on calculating all possible future moves and corresponding states. It thus will always play the most optimal move every time. Certain modifications result in it selecting the shortest path if all moves give the same result.
