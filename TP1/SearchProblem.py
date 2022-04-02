import Tree

algorithmTypes = {
  "breadth": 0,
  "depth": 1,
  "depth_cut": 2,
  "iterative_deepening": 3,
  "uniform": 4,
  "greedy": 5,
  "A*": 6,
}

class SearchProblem:
  def __init__(self, initState, isFinalState):
    self.initState = initState
    self.queue = [Tree.Node(initState, 0, 0, 0, -1)]
    self.isFinalState = isFinalState
    self.visited = []
  
  def getPath(self, node: Tree.Node):
    path = []
    currentNode = node
    while currentNode.parent != -1:
      path.insert(0, currentNode.state)
      currentNode = currentNode.parent
    path.insert(0, currentNode.state)
    return path
  
  def sortQueue(self, algorithm):
    if algorithm == algorithmTypes["breadth"]:
      self.queue.sort(key=lambda node: node.depth)
    elif algorithm == algorithmTypes["depth"]:
      self.queue.sort(key=lambda node: -node.depth)
    elif algorithm == algorithmTypes["depth_cut"]:
      self.queue.sort(key=lambda node: -node.depth)
    elif algorithm == algorithmTypes["iterative_deepening"]:
      self.queue.sort(key=lambda node: -node.depth)
    elif algorithm == algorithmTypes["uniform"]:
      self.queue.sort(key=lambda node: node.cost)
    elif algorithm == algorithmTypes["greedy"]:
      self.queue.sort(key=lambda node: node.heuristic)
    elif algorithm == algorithmTypes["A*"]:
      self.queue.sort(key=lambda node: node.cost + node.heuristic)

  def search(self, newTransitions, heuristic, algorithm, cut=-1):
    totalNodesVisited = 0
    while True:
      if not self.queue:
        print("No solution found!")
        return (None, totalNodesVisited)

      currentNode = self.queue.pop(0)
      totalNodesVisited += 1
      currentState = currentNode.state
      print("currentState:", currentState)

      self.visited.append(str(currentState))
      
      if self.isFinalState(currentState):
        break

      currTransitions = newTransitions(currentNode, heuristic, cut)
      currTransitions = list(filter(lambda transition : str(transition.state) not in self.visited, currTransitions))

      for transition in currTransitions:
        self.queue.append(transition)
      
      self.sortQueue(algorithm)
    
    path = self.getPath(currentNode)
    return (path, totalNodesVisited)

class SearchProblemsAlgorithms:
  def __init__(self, initState, isFinalState, newTransitions):
    self.initState = initState
    self.isFinalState = isFinalState
    self.newTransitions = newTransitions
  
  def showSolution(self, path, totalNodesVisited):
    print("Search path:")
    if (path == None):
      print("No path found")
    else:
      for state in path:
        print(state)
      print("Solution depth:", len(path)-1)
    print("Nodes visited:", totalNodesVisited)

  def breadth(self):
    print("Calculating Breadth solution...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, -1, algorithmTypes["breadth"])

  def depth(self):
    print("Calculating Depth solution...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, -1, algorithmTypes["depth"])

  def depth_cut(self, cut):
    print("Calculating Depth Cut solution for cut", cut, "...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, -1, algorithmTypes["depth_cut"], cut)

  def iterative_deepening(self):
    print("Calculating Iterative Deepening solution...")
    cut = 1
    totalNodesVisited = 0
    while True:
      (path, tnv) = self.depth_cut(cut)
      cut += 1
      totalNodesVisited += tnv
      if (path != None):
        break
    return (path, totalNodesVisited)

  def uniform(self):
    print("Calculating Uniform Cost solution...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, -1, algorithmTypes["uniform"])

  def greedy(self, heuristic):
    print("Calculating Greedy solution for heuristic", heuristic, "...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, heuristic, algorithmTypes["greedy"])

  def aStar(self, heuristic):
    print("Calculating A* solution for heuristic", heuristic, "...")
    solution = SearchProblem(self.initState, self.isFinalState)
    return solution.search(self.newTransitions, heuristic, algorithmTypes["A*"])


  def run(self, algorithm, cut=-1, heuristic=0):
    if algorithmTypes[algorithm] == algorithmTypes["breadth"]:
      res = self.breadth()
    elif algorithmTypes[algorithm] == algorithmTypes["depth"]:
      res = self.depth()
    elif algorithmTypes[algorithm] == algorithmTypes["depth_cut"]:
      res = self.depth_cut(cut)
    elif algorithmTypes[algorithm] == algorithmTypes["iterative_deepening"]:
      res = self.iterative_deepening()
    elif algorithmTypes[algorithm] == algorithmTypes["uniform"]:
      res = self.uniform()
    elif algorithmTypes[algorithm] == algorithmTypes["greedy"]:
      res = self.greedy(heuristic)
    elif algorithmTypes[algorithm] == algorithmTypes["A*"]:
      res = self.aStar(heuristic)
    
    (path, totalNodesVisited) = res
    self.showSolution(path, totalNodesVisited)
