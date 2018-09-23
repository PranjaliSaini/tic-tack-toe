# tic_tack_toe
this is a tick tack toe game played between 2 players

Tick-Tac-Toe game state is defined as follows: 
tile1 |  tile2  | tile3
________________________
tile4 |  tile5  | tile6
________________________
tile7 |  tile8  | tile9
_________________________
A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy
that an intelligent player can take.
We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability
of winning for player1. Assume player1 starts the game.
Game2: A number of games are played between a naive and intelligent player.
Estimate probability of winning for player1. Assume player1 is naive and starts the game.
Game3: A number of games are played between two intelligent players. 
Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random 
There are 2 players: player1 and player2
There are 9 tiles numbered tile0 to tile9
0 value of a tile indicates that tile has not been ticked
1 value indicates that the tile is ticked by player-1
2 value indicates that the tile is ticked by player-2
