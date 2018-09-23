#Sakshi saini
# 2017092


#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random 
# There are 2 players: player1 and player2
player1=1
player2=2

board='012345678'

# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2
random.seed(8)
def drawboard():
	global board
	board='012345678'
	return board

	tile1= board[0]    
	tile2= board[1]
	tile3= board[2]
	tile4= board[3]
	tile5= board[4]
	tile6= board[5]
	tile7= board[6]
	tile8= board[7]
	tile9= board[8]

# turn variable defines whose turn is now
#turn = Player1


def validmove(move):
	#board=drawboard()
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	global board
	if board[move]!='x' and board[move]!='o':
		return True
	else:
		return False


def takemove(board,char,move):
	if validmove(move):
		board=board.replace(board[move],char)
		return(board)


def dupBoard():
	global board
	newboard=''
	for i in board:
		newboard+=i

	return newboard

def checkLine(board,char,spot1,spot2,spot3):
		if board[spot1]==char and board[spot2]==char and board[spot3]==char:
			return(True)
		else:
			return False


def win(board,char):
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	if checkLine(board,char,0,1,2):
		return(True)
	if checkLine(board,char,1,4,7):
		return True
	if checkLine(board,char,2,5,8):
		return True
	if checkLine(board,char,6,7,8):
		return True
	if checkLine(board,char,3,4,5):
		return True
	if checkLine(board,char,1,2,3):
		return True
	if checkLine(board,char,0,3,6):
		return True
	if checkLine(board,char,2,4,6):
		return True
	else:
		return False

	
def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	f=0
	while f==0:
		NaiveMove=random.randint(0,8)
		if validmove(NaiveMove)==True:
			return(NaiveMove)
			f=1
			break

def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	
	"""
	global board
	f=0
	for i in range(9):
		newboard=dupBoard()
		newboard1=dupBoard()
		if validmove(i)==True and f==0 and i%2==0:
			newboard=newboard.replace(newboard[i],'x')
			if win(newboard,'x')==True:
				return(i)
				f=1
			else:
				newboard=newboard.replace(newboard[i],str(i))

	for i in range(9):
		if validmove(i)==True and f==0:
			newboard1=newboard1.replace(newboard1[i],'o')
			if win(newboard1,'o')==True:
				return(i)
				f=1
			else:
				newboard1=newboard1.replace(newboard1[i],str(i))


	if validmove(0) and f==0:
		return(0)
	elif validmove(4) and f==0:
		return(4)
	elif validmove(2) and f==0:
		return(2)
	elif validmove(6) and f==0:
		return(6)
	elif validmove(8) and f==0:
		return(8)
	elif validmove(3) and f==0:
		return(3)
	elif validmove(1) and f==0:
		return(1)
	elif validmove(5) and f==0:
		return (5)
		

def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""

	if board.count('x')==board.count('o') or board.count('x')+1==board.count('o'):
		return True

	else:
		return False
	

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	global board
	if gametype==1:
		board=drawboard()
		gameOn=True
		turn='player1'
		while gameOn==True:
			if turn=='player1':
				move1=takeNaiveMove()
				board=takemove(board,'x',move1)
				if win(board,'x'):
					board=drawboard()
					return(1)
					gameOn=False

				else:
					if board.count('x')+board.count('o')>=8:
						board=drawboard()
						return(0)
						
						gameOn=False
						break

					else:
						turn='player2'

			else:
				move=takeNaiveMove()
				board=takemove(board,'o',move)

				if win(board,'o'):
					board=drawboard()
					return(2)
					gameOn=False
				else:
					if board.count('x')+board.count('o')>=8:
						board=drawboard()
						return(0)
						gameOn=False
						break

					else:
						turn='player1'
	if gametype==2:
		board=drawboard()
		gameOn=True
		turn='player1'
		while gameOn==True:
			if turn=='player1':
				move1=takeNaiveMove()
				board=takemove(board,'o',move1)
				if win(board,'o'):
					board=drawboard()
					return(1)
					gameOn=False

				else:
					if board.count('x')+board.count('o')>=8:
						board=drawboard()
						return(0)
						gameOn=False
						break

					else:
						turn='player2'

			else:
				move=takeStrategicMove()
				board=takemove(board,'x',move)

				if win(board,'x'):
					board=drawboard()
					return(2)
					gameOn=False
				else:
					if board.count('x')+board.count('o')>=8:
						board=drawboard()
						return(0)
						gameOn=False
						break

					else:
						turn='player1'
	

	if gametype==3:
		board=drawboard()
		gameOn=True
		turn='player1'
		while gameOn==True:
			if turn=='player1':
				move1=takeStrategicMove()
				board=takemove(board,'x',move1)
				if win(board,'x'):
					board=drawboard()
					return(1)
					gameOn=False

				else:
					if board.count('x')+board.count('o')>=8:
						board=drawboard()
						return(0)
						gameOn=False
						break

					else:
						turn='player2'

			else:
				move=takeStrategicMove()
				board=takemove(board,'o',move)
				if win(board,'o'):
					board=drawboard()
					return(2)
					gameOn=False
				else:
					if board.count('x')+board.count('o')>=8:
						board=drawboard()
						return(0)
						gameOn=False
						break

					else:
						turn='player1'		
	
def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	cnt=0
	for i in range(n):
		randomGame=game(1)
		if randomGame==1:
			cnt+=1
		else:
			cnt+=0
	prob=cnt/n
	return('prob=%5.4f' %prob)


def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	cnt=0
	for i in range(n):
		randomGame=game(2)
		if randomGame==1:
			cnt+=1
		else:
			cnt+=0
	prob=cnt/n
	print('prob=%5.4f' %prob)

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	cnt=0
	for i in range(n):
		randomGame=game(3)
		if randomGame==1:
			cnt+=1
		else:
			cnt+=0
	prob=cnt/n
	return('prob=%5.4f' %prob)
