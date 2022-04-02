from Algorithms import SearchProblemsAlgorithms
import UnequalLengthMazes as ULM


def showMenu():
  print("\n*          MENU         *")
  print("*-----------------------*")
  print("1 - Upload Puzzle")
  print("2 - Show Current Puzzle")
  print("3 - Solve Puzzle by myself")
  print("4 - Solve Puzzle by AI")
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
  print("0 - Back")

def solvePuzzle(problem):
  algorithm = 1
  while (algorithm != 0):
    showAlgorithms()
    algorithm = int(input("\nOption: "))

    if (algorithm == 1):
      problem.run("breadth")
    elif (algorithm == 2):
      problem.run("depth")
    elif (algorithm == 3):
      limit = int(input("\nDepth Limit: "))
      problem.run("depth_limited", limit=limit)
    elif (algorithm == 4):
      problem.run("iterative_deepening")
    elif (algorithm == 5):
      problem.run("uniform")
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
    else:
      return -1

def main():
  problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
  
  option = 1
  while (option != 0):
    showMenu()
    option = int(input("\nOption: "))

    if (option == 1): print("Temporarily unavailable")
    elif (option == 2): print("Temporarily unavailable")
    elif (option == 3): print("Temporarily unavailable")
    elif (option == 4): solvePuzzle(problem)
    else: exit()

if __name__=='__main__':
  main()