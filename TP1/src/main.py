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
  SOLVE = 4
  END = 5


menusULM = {
  "main_menu" : ("ULM", ['Choose Puzzle', 'Solve Puzzle by myself', 'Solve Puzzle by AI', 'Exit']),
  "algorithms": ("Algorithm", ['Breadth First Search', 'Depth First Search', 'Limited Depth First Search', 'Iterative Deepening', 'Uniform Cost', 'Greedy Algorithm', 'A* Algorithm', 'Back']),
  # "heuristics": ("Heuristics", ['Inverse of the distance of Manhattan from the last move position to the top right corner of the puzzle', 'Sum of each visited cell value. The value of a cell is a multiplication between its row and col.', 'Back']),
  "heuristics": ("Heuristics", ['Inverse of the distance of Manhattan', 'Sum of each visited cell value (row X col weight)', 'Back']),
  # TODO nas heuristicas optar por mais pequeno o texto ou adaptar a funcao de desenhar para mudar de linha!
}

def drawText(text, font, color, surface, x, y):
  textObj = font.render(text, 1, color)
  textRect = textObj.get_rect()
  textRect.topleft = (x, y)
  surface.blit(textObj, textRect)

def drawMenu(menu):

  (title, values) = menu
  indexes = list(range(1, len(values), 1)) + [0]
  options = [str(op[0]) + ' - ' + op[1] for op in list(zip(indexes, values))]
  
  # TODO to remove when read input is correct
  print("\n*          " + title + "         *")
  print("*-----------------------*")
  for option in options:
    print(option)

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


def solvePuzzle(problem): 
  algorithm = 1
  while (algorithm != 0):
    drawMenu(menusULM["algorithms"])
    algorithm = int(input("\nOption: ")) # TODO procced according to the option received 

    if   (algorithm == 1):  problem.run("breadth")
    elif (algorithm == 2):  problem.run("depth")
    elif (algorithm == 3):
      limit = int(input("\nDepth Limit: "))
      problem.run("depth_limited", limit=limit)
    elif (algorithm == 4):  problem.run("iterative_deepening")
    elif (algorithm == 5):  problem.run("uniform")
    elif (algorithm == 6):
      drawMenu(menusULM["heuristics"])
      heuristic = int(input("\nOption: ")) # TODO procced according to the option received
      if (heuristic <= 0): continue
      problem.run("greedy", heuristic=heuristic)
    elif (algorithm == 7):
      drawMenu(menusULM["heuristics"])
      heuristic = int(input("\nOption: "))
      if (heuristic <= 0): continue
      problem.run("A*", heuristic=heuristic)
    else: return -1


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

# Main Menu
def menuState():
  drawMenu(menusULM["main_menu"]) 
  ask = True
  while ask:
    ask = False
    try: option = int(input("\nOption: ")) # TODO do not read from console but from window
    except: ask = True
  if (option == 1): # Change state in the machine
    return State.CHOOSE_BOARD
  elif (option == 2):
    return State.RESOLVE
  elif (option == 3):
    return State.SOLVE
  else:
    return State.END

# Display all possible boards and the player chooses from where
def chooseBoardState(stack):
  n = int(input("\nPuzzle: ")) # TODO make a showBoards which draw all boards, then read the option here
  ULM.setInitState(n)
  stack.clear()
  stack.append(deepcopy(ULM.initState))
  return State.MENU

# Player Solves by him self # add here a space for error message and actions explanation
def resolveState(stack):
  if ULM.isFinalState(stack[-1]): return State.MENU
  else: return State.RESOLVE

# Aks the algorithm to solve the puzzle by
def solveState():
  problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
  solvePuzzle(problem)
  return State.MENU

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


def main():
  pygame.init()
  global screen, font
  
  pygame.display.set_caption('Unequal Length Mazes')
  screen = pygame.display.set_mode((WIDTH, HEIGHT))  
  font = pygame.font.SysFont(None, FONT_SIZE)

  appState = State.MENU
  ULM.setInitState(0) # Default Board
  stack = []
  stack.append(deepcopy(ULM.initState))

  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        appState = State.END
        break
      if appState == State.RESOLVE:
        resolveStateEventHandler(event, stack)
    
    if   appState == State.MENU:          appState = menuState()
    elif appState == State.CHOOSE_BOARD:  appState = chooseBoardState(stack)      
    elif appState == State.RESOLVE:       appState = resolveState(stack)
    elif appState == State.SOLVE:         appState = solveState()
    elif appState == State.END:           run = False
    #draw(screen, stack[-1][0]) # make the draw according ...
      
  pygame.quit()

  
if __name__=='__main__':
  main()