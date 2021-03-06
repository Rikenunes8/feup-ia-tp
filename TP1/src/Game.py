import time
import pygame
import UnequalLengthMazes as ULM
from enum import Enum
from copy import deepcopy
from boards import boardsULM
from Algorithms import SearchProblemsAlgorithms

'''Structure used to keep track of transitions between menus and states in the game (aka State Machine)'''
class State(Enum):
  MENU = 1
  CHOOSE_BOARD = 2
  RESOLVE = 3
  ALGORITHM = 4
  HEURISTIC = 5
  LIMIT = 6
  SOLVE = 7
  SHOW_SOLUTION = 8
  ANALYSE = 9
  END = 10

PENALITY = 20

class Game:
  def __init__(self):
    pygame.init()

    ULM.setInitState(0) # Default Board
    self.stack = [deepcopy(ULM.initState)]
    self.algorithm = None
    self.heuristic = 0
    self.limit = 3
    self.limitStr = ""
    self.solutionAI = None
    
    # Solitaire Game Attributes
    self.initTime = None
    self.elapsedTime = None
    self.playing = False
    self.hint = ''
    self.hintsUsed = 0
    self.score = 0

  def end(self):
    pygame.quit()
  
  def calculateHint(self):
    '''Generate the message of the hint to show according to the solution found and player resolution current state'''
    path = self.solutionAI[0] if self.solutionAI != None else None
    strStack = list(map(lambda x: str(x), self.stack))
    
    # If the solution is not built yet or the partial build is not enough to get a hint then run AI solving algorithm
    if path == None or str(path[0]) not in strStack:
      problem = SearchProblemsAlgorithms(self.stack[-1], ULM.isFinalState, ULM.newTransitions)
      problem.run('greedy', heuristic=3)
      self.solutionAI = problem.getSolution()
      if self.solutionAI[0] == None:
        s = 'back'
      else:
        s = self.solutionAI[0][1][1][2]
    else: # Search on problem solution path already built a hint
      strStack = strStack[strStack.index(str(path[0])):]
      f = list(map(lambda x: x[0] == str(x[1]), zip(strStack, path)))
      if all(f):
        s = path[len(f)][1][2]
      else:
        s = 'back'
    self.hint = s.upper()
    self.hintsUsed += 1

  def makeMove(self, direction):
    '''When a swap is done also move on that direction
    No swap operator state is left on top of the stack'''
    ret1 = ULM.swap(self.stack[-1], direction)
    if ret1:
      self.stack.append(ret1["state"])
    ret2 = ULM.move(self.stack[-1], direction)
    if ret2:
      self.stack.append(ret2["state"])

    if ret1 and (not ret2):
      self.stack.pop()

  def undoMove(self):
    '''Remove from stack until the starting state or the last state got with move operator.
    No swap operator is left on top of the stack.'''
    if len(self.stack) == 1: return    
    self.stack.pop()
    while True and self.stack:
      (board, (x, y, d, l), last) = self.stack[-1]
      if l != 0 or last == None:
        break
      self.stack.pop() 


  def resolveState(self):
    '''The player solves the puzzle by himself'''
    if ULM.isFinalState(self.stack[-1]):
      self.playing = False
    elif not self.playing:
      self.playing = True
      self.initTime = time.time()
      self.hintsUsed = 0
    else: 
      self.elapsedTime = round(time.time() - self.initTime)
      self.score = self.elapsedTime + self.hintsUsed*PENALITY

    return State.RESOLVE
  
  def solveState(self):
    '''The puzzle solution is calculated by the AI according to the algorithm choosen before'''
    problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
    problem.run(self.algorithm, heuristic=self.heuristic, limit=self.limit)
    problem.showSolution()
    self.solutionAI = problem.getSolution()
    return State.SHOW_SOLUTION

  # ----- Event Handlers for each state --------
  
  def mainMenuStateEventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        return State.CHOOSE_BOARD
      elif event.key == pygame.K_2:
        return State.RESOLVE
      elif event.key == pygame.K_3:
        return State.ALGORITHM
      elif event.key == pygame.K_4:
        return State.ANALYSE
      elif event.key == pygame.K_0:
        return State.END
    return State.MENU

  def chooseBoardStateEventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key >= pygame.K_a and event.key <= (pygame.K_a + len(boardsULM) - 1):
        ULM.setInitState(boardsULM[event.key-pygame.K_a])
        self.solutionAI = None
        self.stack.clear()
        self.stack.append(deepcopy(ULM.initState))
        return State.MENU
      elif event.key == pygame.K_ESCAPE:
        return State.MENU
    return State.CHOOSE_BOARD

  def resolveStateEventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      self.hint = ''
      if event.key == pygame.K_ESCAPE:
        self.stack.clear()
        self.stack.append(deepcopy(ULM.initState))
        self.playing = False
        return State.MENU
      if not self.playing: return State.RESOLVE

      if event.key == pygame.K_UP:      self.makeMove("up")
      elif event.key == pygame.K_DOWN:  self.makeMove("down")
      elif event.key == pygame.K_LEFT:  self.makeMove("left")
      elif event.key == pygame.K_RIGHT: self.makeMove("right")
      elif event.key == pygame.K_BACKSPACE: self.undoMove()
      elif event.key == pygame.K_h:     self.calculateHint()
    return State.RESOLVE

  def algorihtmMenuStateEventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        self.algorithm = "breadth"
        return State.SOLVE
      elif event.key == pygame.K_2:
        self.algorithm = "depth"
        return State.SOLVE
      elif event.key == pygame.K_3:
        self.algorithm = "depth_limited"
        return State.LIMIT
      elif event.key == pygame.K_4:
        self.algorithm = "iterative_deepening"
        return State.SOLVE
      elif event.key == pygame.K_5:
        self.algorithm = "uniform"
        return State.SOLVE
      elif event.key == pygame.K_6:
        self.algorithm = "greedy"
        return State.HEURISTIC
      elif event.key == pygame.K_7:
        self.algorithm = "A*"
        return State.HEURISTIC
      elif event.key == pygame.K_0:
        return State.MENU
    return State.ALGORITHM

  def heuristicMenuStateEventHandler(self, event): 
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        self.heuristic = 1
        return State.SOLVE
      elif event.key == pygame.K_2:
        self.heuristic = 2
        return State.SOLVE
      elif event.key == pygame.K_3:
        self.heuristic = 3
        return State.SOLVE
      elif event.key == pygame.K_0:
        return State.ALGORITHM
    return State.HEURISTIC

  def limitStateEventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        self.limitStr = ""
        return State.ALGORITHM
      elif event.key == pygame.K_RETURN:
        if self.limitStr and self.limitStr.isdigit():
          self.limit = int(self.limitStr)
          self.limitStr = ""
          return State.SOLVE
      elif event.key == pygame.K_BACKSPACE:
        self.limitStr = self.limitStr[:-1]
      else:
        self.limitStr += event.unicode
    return State.LIMIT

  def showSolutionStateEventHandler(self, event): 
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return State.ALGORITHM
    return State.SHOW_SOLUTION

  def genericEventHandler(self, appState, event):
    if appState == State.MENU: 
      appState = self.mainMenuStateEventHandler(event)
    elif appState == State.CHOOSE_BOARD:
      appState = self.chooseBoardStateEventHandler(event)
    elif appState == State.RESOLVE:
      appState = self.resolveStateEventHandler(event)
    elif appState == State.ALGORITHM: 
      appState = self.algorihtmMenuStateEventHandler(event)
    elif appState == State.HEURISTIC: 
      appState = self.heuristicMenuStateEventHandler(event)
    elif appState == State.LIMIT:
      appState = self.limitStateEventHandler(event)
    elif appState == State.SHOW_SOLUTION: 
      appState = self.showSolutionStateEventHandler(event)
    return appState