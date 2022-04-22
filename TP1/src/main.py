import pygame
from Game import *
from Drawer import Drawer
from Analyser import Analyser

menusULM = {
  "main_menu" : ("Unequal Length Mazes", ['Choose Puzzle', 'Solve Puzzle by myself', 'Solve Puzzle by AI', 'Comparative Analysis', 'Exit']),
  "algorithms": ("Algorithm", ['Breadth First Search', 'Depth First Search', 'Limited Depth First Search', 'Iterative Deepening', 'Uniform Cost', 'Greedy Algorithm', 'A* Algorithm', 'Back']),
  "heuristics": ("Heuristics", ['Inverse of the distance of Manhattan from last move', 'Sum of each visited cell value (row X col weight)', 'Forbid Dead End States', 'Back']),
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
      appState = game.genericEventHandler(appState, event)
    
    if   appState == State.MENU:          
      drawer.drawOptionMenu(menusULM["main_menu"])
    elif appState == State.CHOOSE_BOARD:
      drawer.drawChooseBoardMenu()
    elif appState == State.RESOLVE:
      drawer.drawResolveState(game.stack[-1][0], game.elapsedTime, len(game.stack)>1 and not game.playing)
      appState = game.resolveState()
    elif appState == State.ALGORITHM:
      drawer.drawOptionMenu(menusULM["algorithms"])
    elif appState == State.HEURISTIC:     
      drawer.drawOptionMenu(menusULM["heuristics"])
    elif appState == State.LIMIT:
      drawer.drawLimitState(game.limitStr)
    elif appState == State.SOLVE:         
      drawer.drawSolveState(game.algorithm, game.heuristic, game.limit)
      appState = game.solveState()
    elif appState == State.SHOW_SOLUTION: 
      drawer.drawSolutionAI(game.solutionAI, game.algorithm, game.heuristic, game.limit)
    elif appState == State.ANALYSE: 
        drawer.drawAnalyseState()
        analyser.analyse(len(menusULM["heuristics"][1])-1)
        appState = State.MENU
    elif appState == State.END:
      run = False
      
  game.end()

  
if __name__=='__main__':
  main()