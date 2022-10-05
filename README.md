# Tic Tac Toe AI Game Development

This is a game created on Python of the famous Tic Tac Toe game. The AI wins a considerable of times. The game is a bit monotonous i.e. the AI will make the same moves for same input given.

This is the position of the game moves user can input:
0   1   2           _   _   _
3   4   5     =>    _   _   _
6   7   8           _   _   _

This is the list of preferred order of moves taken by AI.
- Wins immediately
- Prevents an immediate loss
- Places AI in 1 move away from a win
- Prevents user from being a single move away from win.
- First possible move from position 0 to position 8.
