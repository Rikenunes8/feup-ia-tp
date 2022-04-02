import Tree
from copy import deepcopy

EC = 0
VC = 1
BC = 9

initBoard = [[EC, EC, BC, BC, EC, EC],
             [EC, EC, EC, EC, EC, BC],
             [EC, EC, EC, EC, EC, EC],
             [EC, EC, EC, EC, EC, EC],
             [EC, EC, EC, EC, EC, EC],
             [VC, EC, EC, EC, EC, EC]]

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
  'up': (-1, 0),
  'down': (1, 0),
  'left': (0, -1),
  'right': (0, 1)
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
  step = propDir[direction]
  if edge(direction, row, col) and dir == direction and board[row+step[0]][col+step[1]] == EC:
    row += step[0]
    col += step[1]
    board[row][col] = VC
    length += 1
    return {"state": (board, (row,col,dir,length), lastSegment), "cost": 1}
  return False

def swap(state, direction):
  (board, (row,col,dir,length), lastSegment) = deepcopy(state)
  if ((length != lastSegment and length != 0 and canSwap(direction, dir)) or lastSegment == None):
    dir = direction
    lastSegment = length
    length = 0
    return {"state": (board, (row,col,dir,length), lastSegment), "cost": 0}
  return False



def heuristics(state, type):
  '''Function with the different heuristics that can be used. '''
  def manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

  (_, (row, col, _, _), _) = state
  if type == 1:
    dist = manhattan(row, col, 0, W-1)
    if dist == 0: return 0
    else: return 1/dist
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