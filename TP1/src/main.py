import pygame
from Game import *
from Drawer import Drawer
from analysis import Analyser


menusULM = {
  "main_menu" : ("ULM", ['Choose Puzzle', 'Solve Puzzle by myself', 'Solve Puzzle by AI', 'Comparative Analysis', 'Exit']),
  "algorithms": ("Algorithm", ['Breadth First Search', 'Depth First Search', 'Limited Depth First Search', 'Iterative Deepening', 'Uniform Cost', 'Greedy Algorithm', 'A* Algorithm', 'Back']),
  # "heuristics": ("Heuristics", ['Inverse of the distance of Manhattan from the last move position to the top right corner of the puzzle', 'Sum of each visited cell value. The value of a cell is a multiplication between its row and col.', 'Back']),
  "heuristics": ("Heuristics", ['Inverse of the distance of Manhattan', 'Sum of each visited cell value (row X col weight)', 'Back']),
}

def main():
  game = Game()  
  drawer = Drawer()
  analyser = Analyser()

  drawer.drawOptionMenu(menusULM["main_menu"])
  appState = State.MENU

  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        appState = State.END
        break
      lastState = appState
      if appState == State.MENU: 
        appState = game.mainMenuStateEventHandler(event)
      elif appState == State.CHOOSE_BOARD:
        appState = game.chooseBoardStateEventHandler(event)
      elif appState == State.RESOLVE:
        appState = game.resolveStateEventHandler(event)
      elif appState == State.ALGORITHM: 
        appState = game.algorihtmMenuStateEventHandler(event)
      elif appState == State.HEURISTIC: 
        appState = game.heuristicMenuStateEventHandler(event)
      elif appState == State.SOLVE:
        continue
      elif appState == State.SHOW_SOLUTION: 
        appState = game.showSolutionStateEventHandler(event)
      if (appState != lastState): break
    
    if   appState == State.MENU:          
      drawer.drawOptionMenu(menusULM["main_menu"])
    elif appState == State.CHOOSE_BOARD:  
      drawer.drawChooseBoardMenu()
    elif appState == State.RESOLVE:       
      drawer.drawResolveState(game.stack[-1][0])
      appState = game.resolveState()
    elif appState == State.ALGORITHM:     
      drawer.drawOptionMenu(menusULM["algorithms"])
    elif appState == State.HEURISTIC:     
      drawer.drawOptionMenu(menusULM["heuristics"])
    elif appState == State.SOLVE:         
      drawer.drawSolveState(game.algorithm, game.heuristic)
      appState = game.solveState()
    elif appState == State.SHOW_SOLUTION: 
      drawer.drawSolutionAI(game.solutionAI, game.algorithm, game.heuristic)
    elif appState == State.ANALYSE: 
        drawer.drawAnalyseState()
        analyser.analyse(len(menusULM["heuristics"][1])-1)
        appState = State.MENU
    elif appState == State.END:
      run = False
      
  game.end()

  
if __name__=='__main__':
  main()