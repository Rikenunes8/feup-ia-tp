import pygame
import UnequalLengthMazes as ULM
from enum import Enum
from copy import deepcopy
from Algorithms import SearchProblemsAlgorithms

BG_COLOR = '#888888'
# Board Colors
EMPTY_COLOR = '#DDDDDD'
BLOCK_COLOR = '#000000'
PATH_COLOR = '#FF0000'
# Menu Colors
TITLE_COLOR = '#000000'
BUTTON_COLOR = '#FFFFFF'
TEXT_COLOR = '#000000'

WIDTH, HEIGHT, FONT_SIZE = 800, 600, 40  
screen = ""
font = ""

class State(Enum):
  MENU = 1
  CHOOSE_BOARD = 2
  RESOLVE = 3
  ALGORITHM = 4
  HEURISTIC = 5
  SOLVE = 6
  SHOW_SOLUTION = 7
  END = 8

menusULM = {
  "main_menu" : ("ULM", ['Choose Puzzle', 'Solve Puzzle by myself', 'Solve Puzzle by AI', 'Exit']),
  "algorithms": ("Algorithm", ['Breadth First Search', 'Depth First Search', 'Limited Depth First Search', 'Iterative Deepening', 'Uniform Cost', 'Greedy Algorithm', 'A* Algorithm', 'Back']),
  # "heuristics": ("Heuristics", ['Inverse of the distance of Manhattan from the last move position to the top right corner of the puzzle', 'Sum of each visited cell value. The value of a cell is a multiplication between its row and col.', 'Back']),
  "heuristics": ("Heuristics", ['Inverse of the distance of Manhattan', 'Sum of each visited cell value (row X col weight)', 'Back']),
}

boardsULM = [0, 1, 2, 3, 4]

# TODO arrange better solution
algorithm, heuristic, limit = None, 0, 3 # resolve limit


def drawText(text, font, color, surface, x, y):
  textObj = font.render(text, 1, color)
  textRect = textObj.get_rect()
  textRect.topleft = (x, y)
  surface.blit(textObj, textRect)

def drawMenu(menu):
  (title, values) = menu
  indexes = list(range(1, len(values), 1)) + [0]
  options = [str(op[0]) + ' - ' + op[1] for op in list(zip(indexes, values))]

  screen.fill(BG_COLOR)

  btn_innerX, btn_innerY = 20, 10
  btn_sizeX = font.size(max(options, key = len))[0] + btn_innerX*2
  btn_sizeY = font.size(title)[1] + btn_innerY*2
  offset_x, offset_y = WIDTH/2 - btn_sizeX/2, 30
  
  drawText(title, font, TITLE_COLOR, screen, WIDTH/2 - font.size(title)[0]/2, offset_y)

  offset_y += font.size(title)[1] + FONT_SIZE/2
  for op in options:
    pygame.draw.rect(screen, BUTTON_COLOR, (offset_x, offset_y, btn_sizeX, btn_sizeY)) #offX, offY, sizeX, sizeY
    drawText(op, font, TEXT_COLOR, screen, WIDTH/2 - font.size(op)[0]/2, offset_y + btn_innerY)
    offset_y += btn_sizeY + FONT_SIZE/3

  pygame.display.update()


def drawChooseBoardMenu():
  screen.fill(BG_COLOR)

  offset_x, offset_y = 20, 30

  title = "Choose Board"
  drawText(title, font, TITLE_COLOR, screen, WIDTH/2 - font.size(title)[0]/2, offset_y)

  offset_y += font.size(title)[1] + FONT_SIZE/2
  
  grid_nRows, grid_nCols, grid_margin = 2, 3, 20 # make nRows e nCols vary according to nBoards to display
  row_size = (HEIGHT - offset_y - grid_margin) / grid_nRows
  col_size = (WIDTH - grid_margin) / grid_nCols

  boardIdx = 0
  for row in range(grid_nRows):
    offset_x = grid_margin
    for col in range(grid_nCols):
      if (boardIdx >= len(boardsULM)) : break
      # drawBoard(N, sizeH = row_size - FONT_SIZE, sizeW = col_size - grid_margin) # draw boards in boardsULM N = indexe
      drawText(str(boardIdx), font, TEXT_COLOR, screen, offset_x + col_size/2 - font.size(str(boardIdx))[0], offset_y + row_size - FONT_SIZE)
      boardIdx += 1
      offset_x += col_size
    offset_y += row_size

  pygame.display.update()


# TODO change this to drawBoard with size and offset 
def draw(screen, board):
  rows = len(board)
  cols = len(board[0])
  size = WIDTH / max(rows, cols)

  screen.fill(BG_COLOR)

  for i in range(rows):
    y = size*i
    for j in range(cols):
      x = size*j
      value = board[i][j]
      if value == ULM.BC:
        pygame.draw.rect(screen, BLOCK_COLOR, (x, y, size, size))
      else: 
        pygame.draw.rect(screen, EMPTY_COLOR, (x, y, size, size))
      pygame.draw.rect(screen, "black", (x, y, size, size), 2)
  for i in range(rows):
    y = size*i
    for j in range(cols):
      x = size*j
      value = board[i][j]
      if value == ULM.UP:
        pygame.draw.rect(screen, PATH_COLOR, (x+size/3, y+size*2/6, size/3, size*8/6))
      elif value == ULM.DOWN:
        pygame.draw.rect(screen, PATH_COLOR, (x+size/3, y-size*4/6, size/3, size*8/6))
      elif value == ULM.LEFT:
        pygame.draw.rect(screen, PATH_COLOR, (x+size*2/6, y+size/3, size*8/6, size/3))
      elif value == ULM.RIGHT:
        pygame.draw.rect(screen, PATH_COLOR, (x-size*4/6, y+size/3, size*8/6, size/3))

  pygame.display.update() 



def makeMove(stack, direction):
  ret = ULM.swap(stack[-1], direction)
  if ret:
    stack.append(ret["state"])
  ret = ULM.move(stack[-1], direction)
  if ret:
    stack.append(ret["state"])

def undoMove(stack):
  if len(stack) == 1: return    
  stack.pop()
  while True and stack:
    (board, (x, y, d, l), last) = stack[-1]
    if l != 0 or last == None:
      break
    stack.pop() 


# Player Solves by him self # add here a space for error message and actions explanation
def resolveState(stack):
  draw(screen, stack[-1][0])
  if ULM.isFinalState(stack[-1]): return State.MENU
  else: return State.RESOLVE

# Aks the algorithm to solve the puzzle by
def solveState():
  problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
  problem.run(algorithm, heuristic=heuristic, limit=limit)
  return State.SHOW_SOLUTION

def drawSolutionAI(): # TODO draw_problema solution found by the AI, parameters, path, time, nodes?
  print("solution")

def mainMenuStateEventHandler(event):
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_1:
      return State.CHOOSE_BOARD
    elif event.key == pygame.K_2:
      return State.RESOLVE
    elif event.key == pygame.K_3:
      return State.ALGORITHM
    elif event.key == pygame.K_0:
      return State.END
  return State.MENU

def chooseBoardStateEventHandler(event, stack):
  if event.type == pygame.KEYDOWN:
    if event.key >= pygame.K_0 and event.key <= (pygame.K_0 + len(boardsULM) - 1):
      ULM.setInitState(boardsULM[event.key-48]) 
      stack.clear()
      stack.append(deepcopy(ULM.initState))
      return State.MENU
    elif event.key == pygame.K_ESCAPE:
      return State.MENU
  return State.CHOOSE_BOARD

def resolveStateEventHandler(event, stack):
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
      makeMove(stack, "up")
    elif event.key == pygame.K_DOWN:
      makeMove(stack, "down")
    elif event.key == pygame.K_LEFT:
      makeMove(stack, "left")
    elif event.key == pygame.K_RIGHT:
      makeMove(stack, "right")
    elif event.key == pygame.K_BACKSPACE:
      undoMove(stack)
    elif event.key == pygame.K_ESCAPE:
      stack.clear()
      stack.append(deepcopy(ULM.initState))
      return State.MENU
  return State.RESOLVE

def algorihtmMenuStateEventHandler(event):
  global algorithm
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_1:
      algorithm = "breadth"
      return State.SOLVE
    elif event.key == pygame.K_2:
      algorithm = "depth"
      return State.SOLVE
    elif event.key == pygame.K_3:
      algorithm = "depth_limited"
      return State.SOLVE
    elif event.key == pygame.K_4:
      algorithm = "iterative_deepening"
      return State.SOLVE
    elif event.key == pygame.K_5:
      algorithm = "uniform"
      return State.SOLVE
    elif event.key == pygame.K_6:
      algorithm = "greedy"
      return State.HEURISTIC
    elif event.key == pygame.K_7:
      algorithm = "A*"
      return State.HEURISTIC
    elif event.key == pygame.K_0:
      return State.MENU
  return State.ALGORITHM

def heuristicMenuStateEventHandler(event): 
  global heuristic
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_1:
      heuristic = 1
      return State.SOLVE
    elif event.key == pygame.K_2:
      heuristic = 2
      return State.SOLVE
    elif event.key == pygame.K_0:
      return State.ALGORITHM
  return State.HEURISTIC

def showSolutionStateEventHandler(event): 
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_ESCAPE:
      return State.ALGORITHM
  return State.SHOW_SOLUTION

def main():
  pygame.init()
  global screen, font

  pygame.display.set_caption('Unequal Length Mazes')
  screen = pygame.display.set_mode((WIDTH, HEIGHT))  
  font = pygame.font.SysFont(None, FONT_SIZE)

  appState = State.MENU
  drawMenu(menusULM["main_menu"])

  ULM.setInitState(0) # Default Board
  stack = []
  stack.append(deepcopy(ULM.initState))

  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        appState = State.END
        break
      lastState = appState
      if appState == State.MENU: 
        appState = mainMenuStateEventHandler(event)
      elif appState == State.CHOOSE_BOARD:
        appState = chooseBoardStateEventHandler(event, stack)
      elif appState == State.RESOLVE:
        appState = resolveStateEventHandler(event, stack)
      elif appState == State.ALGORITHM: 
        appState = algorihtmMenuStateEventHandler(event)
      elif appState == State.HEURISTIC: 
        appState = heuristicMenuStateEventHandler(event)
      elif appState == State.SHOW_SOLUTION: 
        appState = showSolutionStateEventHandler(event)
      if (appState != lastState): break

    if   appState == State.MENU:          drawMenu(menusULM["main_menu"])
    elif appState == State.CHOOSE_BOARD:  drawChooseBoardMenu()
    elif appState == State.RESOLVE:       appState = resolveState(stack)
    elif appState == State.ALGORITHM:     drawMenu(menusULM["algorithms"])
    elif appState == State.HEURISTIC:     drawMenu(menusULM["heuristics"])
    elif appState == State.SOLVE:         appState = solveState() # TODO loading window here while computing
    elif appState == State.SHOW_SOLUTION: drawSolutionAI() # TODO
    elif appState == State.END:           run = False
      
  pygame.quit()

  
if __name__=='__main__':
  main()