import time
from SearchProblem import SearchProblem, algorithmTypes

class SearchProblemsAlgorithms:
  def __init__(self, initState, isFinalState, newTransitions):
    self.initState = initState
    self.isFinalState = isFinalState
    self.newTransitions = newTransitions
    self.solution = (None, 0, 0, 0) # path, solution_depth, nodes_visited, elapsed_time

  
  def showSolution(self):
    (path, depth, totalNodesVisited, elapsedTime) = self.solution
    print("Search path:")
    if (path == None):
      print("No path found")
    else:
      for state in path:
        print(state)
      print("Solution depth:", depth)
    print("Nodes visited:", totalNodesVisited)
    print("Elapsed Time:", elapsedTime)

  def getSolution(self):
    return self.solution    

  def breadth(self):
    print("Calculating BFS solution...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, algorithmTypes["breadth"])

  def depth(self):
    print("Calculating DFS solution...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, algorithmTypes["depth"])

  def depth_limited(self, limit):
    print("Calculating DFS Limited solution for limit", limit, "...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, algorithmTypes["depth_limited"], limit=limit)

  def iterative_deepening(self):
    print("Calculating Iterative Deepening solution...")
    limit = 1
    totalNodesVisited = 0
    while True:
      (path, tnv) = self.depth_limited(limit)
      limit += 1
      totalNodesVisited += tnv
      if (path != None):
        break
    return (path, totalNodesVisited)

  def uniform(self):
    print("Calculating Uniform Cost solution...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, algorithmTypes["uniform"])

  def greedy(self, heuristic):
    print("Calculating Greedy solution for heuristic", heuristic, "...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, algorithmTypes["greedy"], heuristic=heuristic)

  def aStar(self, heuristic):
    print("Calculating A* solution for heuristic", heuristic, "...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, algorithmTypes["A*"], heuristic=heuristic)


  def run(self, algorithm, heuristic=0, limit=-1):
    '''Search solution by algorithm, saving the time needed for computation'''
    start_time = time.time()

    if algorithmTypes[algorithm] == algorithmTypes["breadth"]:
      res = self.breadth()
    elif algorithmTypes[algorithm] == algorithmTypes["depth"]:
      res = self.depth()
    elif algorithmTypes[algorithm] == algorithmTypes["depth_limited"]:
      res = self.depth_limited(limit)
    elif algorithmTypes[algorithm] == algorithmTypes["iterative_deepening"]:
      res = self.iterative_deepening()
    elif algorithmTypes[algorithm] == algorithmTypes["uniform"]:
      res = self.uniform()
    elif algorithmTypes[algorithm] == algorithmTypes["greedy"]:
      res = self.greedy(heuristic)
    elif algorithmTypes[algorithm] == algorithmTypes["A*"]:
      res = self.aStar(heuristic)

    (path, totalNodesVisited) = res
    elapsedTime = round(time.time() - start_time, 2)
    self.solution = (path, 0 if path == None else len(path)-1, totalNodesVisited, elapsedTime)
    