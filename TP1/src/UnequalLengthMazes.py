import Tree
import boards
from copy import deepcopy

EC = boards.EC
VC = boards.VC
BC = boards.BC

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

H = 0
W = 0
initState = ()

def setInitState(n):
  global initState, H, W

  initBoard = boards.initBoards[n]
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

propDir = {
  'up': {"step":(-1, 0), "value": UP},
  'down': {"step":(1, 0), "value": DOWN},
  'left': {"step":(0, -1), "value": LEFT},
  'right': {"step":(0, 1), "value": RIGHT}
}

def edge(dir, row, col):
  if dir == 'up':
    return row > 0
  elif dir == 'down':
    return row < H-1
  elif dir == 'left':
    return col > 0
  elif dir== 'right':
    return col < W-1
  return False

def canSwap(nextDir, prevDir):
  if nextDir == 'up' or nextDir == 'down':
    return prevDir == 'left' or prevDir == 'right'
  elif nextDir == 'left' or nextDir == 'right':
    return prevDir == 'up' or prevDir == 'down'
  return False
    

def move(state, direction):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  step = propDir[direction]['step']
  if edge(direction, row, col) and dir == direction and board[row+step[0]][col+step[1]] == EC:
    row += step[0]
    col += step[1]
    board[row][col] = propDir[direction]['value']
    length += 1
    return {"state": (board, (row,col,dir,length), lastSegment), "cost": 1}
  return False

def swap(state, direction):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if ((length != lastSegment and length != 0 and canSwap(direction, dir)) or lastSegment == None):
    dir = direction
    lastSegment = length
    length = 0
    return {"state": (board, (row,col,dir,length), lastSegment), "cost": 2}
  return False

def emptyAdjacents(state, i, j):
  (board, (row, col, d, l), last) = state
  c = 0
  for direction in propDir.keys():
    (offX, offY) = propDir[direction]["step"]
    x, y = i+offX, j+offY
    if edge(direction, x, y) and ((x == row and y == col) or board[x][y] == EC):
      c += 1
  return c

def heuristics(state, type):
  '''Function with the different heuristics that can be used. '''
  def manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

  (board, (row, col, d, l), last) = state
  if type == 1:
    dist = manhattan(row, col, 0, W-1)
    if dist == 0: return 0
    else: return 1/dist
  elif type == 2:
    value = 0
    num_visited = 0
    for i in range(len(board)):
      for j in range(len(board[i])):
        if (board[i][j] == VC):
          num_visited += 1
          value += (H-i)*(j+1)
    return value / num_visited
  elif type == 3:
    emptyCells = 0
    for i in range(len(board)):
      for j in range(len(board[i])):
        if (board[i][j] == EC and (i != 0 and j != W-1)):
          emptyCells += 1
          if emptyAdjacents(state, i, j) < 2:
            return 9999999
    return emptyCells
  return 0

def newTransitions(node: Tree.Node, heuristic):
  '''Find reachable nodes from node. Returns only the values of the nodes to be created on SearchProblem.'''
  state = node.state

  # To change between problems if needed
  transitionsMoves = [move(state, direction) for direction in propDir.keys()] + [swap(state, direction) for direction in propDir.keys()]
  transitionsMoves = list(filter(lambda state : state, transitionsMoves))
  # ------------------------------------

  transitions = []
  for movement in transitionsMoves:
    newState = movement["state"]
    newCost = movement["cost"]
    newHeuristic = heuristics(newState, heuristic)
    transitions.append(Tree.Node(newState, node.depth+1, node.cost+newCost, newHeuristic, node))
  return transitions