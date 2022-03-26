import Tree

algorithmTypes = {
  "breadth": 0,
  "depth": 1,
  "depth_cut": 2,
  "iterative_deepening": 3,
  "uniform": 4,
  "greedy": 5,
  "A*": 6,
  "heuristics": [5, 6]
}

class SearchProblem:
  def __init__(self, initState, isFinalState):
    self.initState = initState
    self.initNode = Tree.Node((initState, 0), -1)
    self.queue = [self.initNode]
    self.isFinalState = isFinalState
    self.visited = []
  
  def getPath(self, node: Tree.Node):
    path = []
    currentNode = node
    while currentNode.prev != -1:
      path.insert(0, currentNode.value)
      currentNode = currentNode.prev
    path.insert(0, currentNode.value)
    return path
  
  def search(self, newTransitions, heuristic, algorithm, cut=-1):
    countNodesVisited = 0
    while True:
      if not self.queue:
        print("No solution found!")
        return False
      currentNode = self.queue.pop(0)
      countNodesVisited += 1
      (currentState, _) = currentNode.value
      print("currentState:", currentState)

      self.visited.append(str(currentState))
      
      if self.isFinalState(currentState):
        break

      currTransitions = newTransitions(currentNode, algorithm, heuristic, cut)
      currTransitions = list(filter(lambda transition : str(transition[0]) not in self.visited, currTransitions))

      for transition in currTransitions:
        self.queue.append(Tree.Node(transition, currentNode))
      
      self.queue.sort(key=lambda node: node.value[1])

    path = self.getPath(currentNode)
    print("Search path:")
    for node in path:
      print(node[0])
    print("Solution depth:", len(path))
    print("Nodes visited:", countNodesVisited)
    return True

class SearchProblemsAlgorithms:
  def __init__(self, initState, isFinalState, newTransitions):
    self.initState = initState
    self.isFinalState = isFinalState
    self.newTransitions = newTransitions
  
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
    while not self.depth_cut(cut):
      cut += 1

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
      self.breadth()
    elif algorithmTypes[algorithm] == algorithmTypes["depth"]:
      self.depth()
    elif algorithmTypes[algorithm] == algorithmTypes["depth_cut"]:
      self.depth_cut(cut)
    elif algorithmTypes[algorithm] == algorithmTypes["iterative_deepening"]:
      self.iterative_deepening()
    elif algorithmTypes[algorithm] == algorithmTypes["uniform"]:
      self.uniform()
    elif algorithmTypes[algorithm] == algorithmTypes["greedy"]:
      self.greedy(heuristic)
    elif algorithmTypes[algorithm] == algorithmTypes["A*"]:
      self.aStar(heuristic)
