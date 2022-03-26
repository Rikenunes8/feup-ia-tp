import Tree
from copy import deepcopy
from SearchProblem import algorithmTypes

EC = 0
VC = 1
BC = 9

board = [[EC, EC, BC, BC, EC, EC],
         [EC, EC, EC, EC, EC, BC],
         [EC, EC, EC, EC, EC, EC],
         [EC, EC, EC, EC, EC, EC],
         [EC, EC, EC, EC, EC, EC],
         [VC, EC, EC, EC, EC, EC]]
board1 = [[BC, BC, EC],
          [EC, EC, EC],
          [VC, BC, BC]]
board2 = [[BC, EC, EC],
          [BC, EC, BC],
          [VC, EC, BC]]

board3 = [[EC, EC, EC, EC],
          [EC, EC, EC, BC],
          [VC, EC, EC, BC]]

initBoard = board
H = len(initBoard)
W = len(initBoard[0])
currentCell = (H-1, 0, None, 0)
lastSegment = None

initState = (initBoard, currentCell, lastSegment)

def isFinalState(state):
  (board, (row,col,dir,length), lastSegment) = state
  for line in board:
    for cell in line:
      if cell == EC:
        return False
  return row == 0 and col == W-1 and length != lastSegment



def up(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if row > 0 and dir == 'up' and board[row-1][col] == EC:
    row -= 1
    board[row][col] = VC
    length += 1
    return (board, (row,col,dir,length), lastSegment)
  return False
  
def down(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if row < H-1 and dir == 'down' and board[row+1][col] == EC:
    row += 1
    board[row][col] = VC
    length += 1
    return (board, (row,col,dir,length), lastSegment)
  return False

def left(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if col > 0 and dir == 'left' and board[row][col-1] == EC:
    col -= 1
    board[row][col] = VC
    length += 1
    return (board, (row,col,dir,length), lastSegment)
  return False
  
def right(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if col < W-1 and dir == 'right' and board[row][col+1] == EC:
    col += 1
    board[row][col] = VC
    length += 1
    return (board, (row,col,dir,length), lastSegment)
  return False

def swapToUp(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if ((length != lastSegment and length != 0 and (dir == 'left' or dir == 'right')) or lastSegment == None):
    dir = 'up'
    lastSegment = length
    length = 0
    return (board, (row,col,dir,length), lastSegment)
  return False

def swapToDown(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if ((length != lastSegment and length != 0 and (dir == 'left' or dir == 'right')) or lastSegment == None):
    dir = 'down'
    lastSegment = length
    length = 0
    return (board, (row,col,dir,length), lastSegment)
  return False

def swapToLeft(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if ((length != lastSegment and length != 0 and (dir == 'up' or dir == 'down')) or lastSegment == None):
    dir = 'left'
    lastSegment = length
    length = 0
    return (board, (row,col,dir,length), lastSegment)
  return False

def swapToRight(state):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if ((length != lastSegment and length != 0 and (dir == 'up' or dir == 'down')) or lastSegment == None):
    dir = 'right'
    lastSegment = length
    length = 0
    return (board, (row,col,dir,length), lastSegment)
  return False

operators = [up, down, left, right, swapToUp, swapToDown, swapToLeft, swapToRight]

def heuristics(state, currCost, type):
  '''Function with the different heuristics that can be used. '''
  return currCost

def newTransitions(node: Tree.Node, algorithm, heuristic, cut=-1):
  '''Find reachable nodes from node. Returns only the values of the nodes to be created on SearchProblem.'''
  state = node.value[0]
  cost = node.value[1] + 1 if algorithm != algorithmTypes["greedy"] else 0
  
  cost = node.value[1] - 1 if algorithm == algorithmTypes["depth"] or algorithm == algorithmTypes["depth_cut"] else cost
  if algorithm == algorithmTypes["depth_cut"] and cut <= -cost:
    return []

  # To change between problems if needed
  transitionsStates = [op(state) for op in operators]
  transitionsStates = list(filter(lambda state : state, transitionsStates))
  # ------------------------------------

  transitions = []
  for state in transitionsStates:
    newCost = heuristics(state, cost, heuristic) if algorithm in algorithmTypes["heuristics"] else cost
    newNode = (state, newCost)
    transitions.append(newNode)
  return transitions