from a2 import validmove
from a2 import takemove
from a2 import checkLine
from a2 import win
from a2 import takeNaiveMove
from a2 import takeStrategicMove
from a2 import validBoard
from a2 import game1
from a2 import game2
from a2 import game3


testboard='012345678'

newboard='012345678'

assert (validmove(1)==True),'The Move is not Valid'
assert (validmove(2)==True),'The Move is not Valid'
assert (validmove(3)==True),'The Move is not Valid'
assert (validmove(4)==True),'The Move is not Valid'



assert(checkLine(testboard,'x',0,1,2)==False),'The board is not repesenting the wining condition'
assert(checkLine(testboard,'x',3,4,5)==False),'The board is not repesenting the wining condition'
assert(checkLine(testboard,'x',6,7,8)==False),'The board is not repesenting the wining condition'
assert(checkLine(testboard,'x',0,4,8)==False),'The board is repesenting the wining condition but the board isin\'t in that condition'


assert(win(testboard,'x')==False),'The board is not showing state of the wining of player'
assert(win(testboard,'o')==False),'The board is not showing state of the wining of player'
assert(win(testboard,'x')==False),'The board is not showing state of the wining of player'

assert(str(takeNaiveMove()) in '12345'),'The return tile must be unmarked'
assert(str(takeNaiveMove()) in '2345'),'The return tile must be unmarked'
assert(str(takeNaiveMove()) in '67345'),'The return tile must be unmarked'


assert(str(takeStrategicMove()) in '02685'),'It must check the corner tile or centre'

assert(validBoard()==True),'No. of tics made by the player 1 must be same of player2 or is +1 of player2'

#assert(game1(4)>=0 and game1(4)<=1),'The probability shold be between 0 and 1'
#assert(game2(40)>=0 and game2(40)<=1),'The probability shold be between 0 and 1'
#assert(game3(50)>=0 and game3(50)<=1),'The probability shold be between 0 and 1'

