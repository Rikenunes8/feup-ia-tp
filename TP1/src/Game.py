import UnequalLengthMazes as ULM
from enum import Enum
from copy import deepcopy
import pygame
import UnequalLengthMazes as ULM
from boards import boardsULM
from Algorithms import SearchProblemsAlgorithms




class State(Enum):
  MENU = 1
  CHOOSE_BOARD = 2
  RESOLVE = 3
  ALGORITHM = 4
  HEURISTIC = 5
  SOLVE = 6
  SHOW_SOLUTION = 7
  END = 8

class Game:
  def __init__(self):
    pygame.init()

    ULM.setInitState(0) # Default Board
    self.stack = []
    self.stack.append(deepcopy(ULM.initState))
    self.algorithm = None
    self.heuristic = 0
    self.limit = 3
    self.solutionAI = None

  def end(self):
    pygame.quit()

  def makeMove(self, direction):
    ret1 = ULM.swap(self.stack[-1], direction)
    if ret1:
      self.stack.append(ret1["state"])
    ret2 = ULM.move(self.stack[-1], direction)
    if ret2:
      self.stack.append(ret2["state"])
    
    if (ret1 and (not ret2)):
      self.stack.pop()

  def undoMove(self):
    if len(self.stack) == 1: return    
    self.stack.pop()
    while True and self.stack:
      (board, (x, y, d, l), last) = self.stack[-1]
      if l != 0 or last == None:
        break
      self.stack.pop() 


  # Player Solves by him self # add here a space for error message and actions explanation
  def resolveState(self):
    if ULM.isFinalState(self.stack[-1]): 
      self.stack = self.stack[:1]
      return State.MENU
    else: return State.RESOLVE

  # Aks the algorithm to solve the puzzle by
  def solveState(self):
    problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
    problem.run(self.algorithm, heuristic=self.heuristic, limit=self.limit)
    self.solutionAI = problem.getSolution()
    return State.SHOW_SOLUTION


  def mainMenuStateEventHandler(self, event):
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

  def chooseBoardStateEventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key >= pygame.K_a and event.key <= (pygame.K_a + len(boardsULM) - 1):
        ULM.setInitState(boardsULM[event.key-pygame.K_a]) 
        self.stack.clear()
        self.stack.append(deepcopy(ULM.initState))
        return State.MENU
      elif event.key == pygame.K_ESCAPE:
        return State.MENU
    return State.CHOOSE_BOARD

  def resolveStateEventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.makeMove("up")
      elif event.key == pygame.K_DOWN:
        self.makeMove("down")
      elif event.key == pygame.K_LEFT:
        self.makeMove("left")
      elif event.key == pygame.K_RIGHT:
        self.makeMove("right")
      elif event.key == pygame.K_BACKSPACE:
        self.undoMove()
      elif event.key == pygame.K_ESCAPE:
        self.stack.clear()
        self.stack.append(deepcopy(ULM.initState))
        return State.MENU
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
        return State.SOLVE
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
      elif event.key == pygame.K_0:
        return State.ALGORITHM
    return State.HEURISTIC

  def showSolutionStateEventHandler(self, event): 
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return State.ALGORITHM
    return State.SHOW_SOLUTION
