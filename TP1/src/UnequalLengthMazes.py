import Tree
import boards
from copy import deepcopy

'''Representation of the board's cells'''
EC = boards.EC
VC = boards.VC
BC = boards.BC

'''Representation of the direction the cell was visited from'''
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

'''Global Variables to store board information and initial state'''
H = 0
W = 0
initState = ()

def setInitState(n):
  '''Initializes start state according to board received'''
  global initState, H, W

  initBoard = boards.initBoards[n]
  H = len(initBoard)
  W = len(initBoard[0])
  currentCell = (H-1, 0, None, 0)
  lastSegment = None
  initState = (initBoard, currentCell, lastSegment)

def isFinalState(state):
  '''Checks if a state is a final state: none empty cell or consecutive segments with same length'''
  (board, (row,col,dir,length), lastSegment) = state
  for line in board:
    for cell in line:
      if cell == EC:
        return False
  return row == 0 and col == W-1 and length != lastSegment

'''Structure that contains needed information regarding each possible direction'''
propDir = {
  'up': {"step":(-1, 0), "value": UP},
  'down': {"step":(1, 0), "value": DOWN},
  'left': {"step":(0, -1), "value": LEFT},
  'right': {"step":(0, 1), "value": RIGHT}
}

def withinBoard(row, col):
  '''Checks if (row, col) are valid coordinates in the current board'''
  return row >= 0 and row < H and col >= 0 and col < W

def canSwap(nextDir, prevDir):
  '''Checks if if possible to change direction: alternate between vertical and horizontal segments'''
  if nextDir == 'up' or nextDir == 'down':
    return prevDir == 'left' or prevDir == 'right'
  elif nextDir == 'left' or nextDir == 'right':
    return prevDir == 'up' or prevDir == 'down'
  return False
    

def move(state, direction):
  '''Apply the operator move if possible: advance to an empty cell in the same direction'''
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  step = propDir[direction]['step']
  row += step[0]
  col += step[1]
  if withinBoard(row, col) and dir == direction and board[row][col] == EC:
    board[row][col] = propDir[direction]['value']
    length += 1
    return {"state": (board, (row,col,dir,length), lastSegment), "cost": 1}
  return False

def swap(state, direction):
  '''Apply the operator swap if possible: change direction when segments have different length'''
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if ((length != lastSegment and length != 0 and canSwap(direction, dir)) or lastSegment == None):
    dir = direction
    lastSegment = length
    length = 0
    return {"state": (board, (row,col,dir,length), lastSegment), "cost": 2}
  return False

def emptyAdjacents(state, i, j):
  '''Return number of empty cells adjacents to cell in (i,j) of state\'s board'''
  (board, (row, col, d, l), last) = state
  c = 0
  for direction in propDir.keys():
    (offX, offY) = propDir[direction]["step"]
    x, y = i+offX, j+offY
    if withinBoard(x, y) and ((x == row and y == col) or board[x][y] == EC):
      c += 1
  return c

def heuristics(state, type):
  '''Function with the different heuristics that can be used according to the type choosen'''
  def manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

  (board, (row, col, d, l), last) = state
  if type == 1: # Inverse of the distance of Manhattan from last move
    dist = manhattan(row, col, 0, W-1)
    if dist == 0: return 0
    else: return 1/dist
  elif type == 2: # Sum of each empty cell value with dead end cuts qualquer
    value = 0
    for i in range(len(board)):
      for j in range(len(board[i])):
        if (board[i][j] == EC):
          value += abs(i-j)
          if (i != 0 and j != W-1) and emptyAdjacents(state, i, j) < 2:
            return 99999
    return value
  elif type == 3: # Number of empty cells with dead end cuts
    emptyCells = 0
    for i in range(len(board)):
      for j in range(len(board[i])):
        if (board[i][j] == EC and (i != 0 and j != W-1)):
          emptyCells += 1
          if emptyAdjacents(state, i, j) < 2:
            return 99999
    return emptyCells * 2
  return 0

def newTransitions(node: Tree.Node, heuristic):
  '''Find reachable states from node\'s state and return nodes correspondig to those states.'''
  state = node.state

  # To change between problems if needed
  transitionsMoves = [move(state, direction) for direction in propDir.keys()] + [swap(state, direction) for direction in propDir.keys()]
  transitionsMoves = list(filter(lambda state : state, transitionsMoves))
  # ------------------------------------

  transitions = []
  # Create Tree node to each transition that can be made
  for movement in transitionsMoves:
    newState = movement["state"]
    newCost = movement["cost"]
    newHeuristic = heuristics(newState, heuristic)
    transitions.append(Tree.Node(newState, node.depth+1, node.cost+newCost, newHeuristic, node))
  return transitions