from Algorithms import SearchProblemsAlgorithms
from copy import deepcopy
import UnequalLengthMazes as ULM
import pygame
from enum import Enum

BG_COLOR = '#888888'
EMPTY_COLOR = '#DDDDDD'
BLOCK_COLOR = '#000000'
PATH_COLOR = '#FF0000'
WIDTH, HEIGHT = 600, 600  

class State(Enum):
  MENU = 1
  CHOOSE_BOARD = 2
  RESOLVE = 3
  SOLVE = 4
  END = 5


def showMenu():
  print("\n*          MENU         *")
  print("*-----------------------*")
  print("1 - Choose Puzzle")
  print("2 - Solve Puzzle by myself")
  print("3 - Solve Puzzle by AI")
  print("0 - Exit")

def showAlgorithms():
  print("\n*       Algorithm       *")
  print("*-----------------------*")
  print("1 - Breadth First Search")
  print("2 - Depth First Search")
  print("3 - Limited Depth First Search")
  print("4 - Iterative Deepening")
  print("5 - Uniform Cost")
  print("6 - Greedy Algorithm")
  print("7 - A* Algorithm")
  print("0 - Back")

def showHeuristics():
  print("\n*      Heuristics       *")
  print("*-----------------------*")
  print("1 - Inverse of the distance of Manhattan from the last move position to the top right corner of the puzzle")
  print("2 - Sum of each visited cell value. The value of a cell is a multiplication between its row and col.")
  print("0 - Back")



def solvePuzzle(problem):
  algorithm = 1
  while (algorithm != 0):
    showAlgorithms()
    algorithm = int(input("\nOption: "))

    if   (algorithm == 1):  problem.run("breadth")
    elif (algorithm == 2):  problem.run("depth")
    elif (algorithm == 3):
      limit = int(input("\nDepth Limit: "))
      problem.run("depth_limited", limit=limit)
    elif (algorithm == 4):  problem.run("iterative_deepening")
    elif (algorithm == 5):  problem.run("uniform")
    elif (algorithm == 6):
      showHeuristics()
      heuristic = int(input("\nOption: "))
      if (heuristic <= 0): continue
      problem.run("greedy", heuristic=heuristic)
    elif (algorithm == 7):
      showHeuristics()
      heuristic = int(input("\nOption: "))
      if (heuristic <= 0): continue
      problem.run("A*", heuristic=heuristic)
    else: return -1



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
  stack.pop()
  while True:
    (board, (x, y, d, l), last) = stack[-1]
    if l != 0 or last == None:
      break
    stack.pop() 


def menuState(stack):
  showMenu()
  option = int(input("\nOption: "))
  if (option == 1): 
    return State.CHOOSE_BOARD
  elif (option == 2): 
    stack.append(deepcopy(ULM.initState))
    return State.RESOLVE
  elif (option == 3):
    return State.SOLVE
  else:
    return State.END

def chooseBoardState():
  return State.MENU

def resolveState(stack):
  if ULM.isFinalState(stack[-1]): return State.MENU
  else: return State.RESOLVE

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
  screen = pygame.display.set_mode((WIDTH, HEIGHT))  
  pygame.display.set_caption('Unequal Length Mazes')

  appState = State.MENU
  stack = []

  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        appState = State.END
        break
      if appState == State.RESOLVE:
        resolveStateEventHandler(event, stack)
        draw(screen, stack[-1][0])
    
    if   appState == State.MENU:          appState = menuState(stack)
    elif appState == State.CHOOSE_BOARD:  appState = chooseBoardState()      
    elif appState == State.RESOLVE:       appState = resolveState(stack)
    elif appState == State.SOLVE:         appState = solveState()
    elif appState == State.END:           run = False
      
  pygame.quit()

  
if __name__=='__main__':
  main()