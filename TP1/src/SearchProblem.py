import Tree
from copy import deepcopy

algorithmTypes = {
  "breadth": 0,
  "depth": 1,
  "depth_limited": 2,
  "iterative_deepening": 3,
  "uniform": 4,
  "greedy": 5,
  "A*": 6,
}

class SearchProblem:
  def __init__(self, initState, isFinalState, checkVisited=False):
    self.initState = deepcopy(initState)
    self.queue = [Tree.Node(initState, 0, 0, 0, -1)]
    self.isFinalState = isFinalState
    self.visited = []
    self.checkVisited = checkVisited
  
  def getPath(self, node: Tree.Node):
    path = []
    currentNode = node
    while currentNode.parent != -1:
      path.insert(0, currentNode.state)
      currentNode = currentNode.parent
    path.insert(0, currentNode.state)
    return path
  
  # def sortQueue(self, algorithm):
  #   if algorithm == algorithmTypes["breadth"]:
  #     self.queue.sort(key=lambda node: node.depth)
  #   elif algorithm == algorithmTypes["depth"]:
  #     self.queue.sort(key=lambda node: -node.depth)
  #   elif algorithm == algorithmTypes["depth_limited"]:
  #     self.queue.sort(key=lambda node: -node.depth)
  #   elif algorithm == algorithmTypes["iterative_deepening"]:
  #     self.queue.sort(key=lambda node: -node.depth)
  #   elif algorithm == algorithmTypes["uniform"]:
  #     self.queue.sort(key=lambda node: node.cost)
  #   elif algorithm == algorithmTypes["greedy"]:
  #     self.queue.sort(key=lambda node: node.heuristic)
  #   elif algorithm == algorithmTypes["A*"]:
  #     self.queue.sort(key=lambda node: node.cost + node.heuristic)

  def lessThanNode(self, algorithm, node1, node2):
    if algorithm == algorithmTypes["breadth"]:
      return node1.depth < node2.depth
    elif algorithm == algorithmTypes["depth"]:
      return -node1.depth < -node2.depth
    elif algorithm == algorithmTypes["depth_limited"]:
      return -node1.depth < -node2.depth
    elif algorithm == algorithmTypes["iterative_deepening"]:
      return -node1.depth < -node2.depth
    elif algorithm == algorithmTypes["uniform"]:
      return node1.cost < node2.cost
    elif algorithm == algorithmTypes["greedy"]:
      return node1.heuristic < node2.heuristic
    elif algorithm == algorithmTypes["A*"]:
      return node1.cost + node1.heuristic < node2.cost + node2.heuristic

  def getInsertPosition(self, algorithm, node):
    if not self.queue: return 0
    lower, higher = 0, len(self.queue)-1
    while lower <= higher:
      mid = (lower + higher) // 2
      if self.lessThanNode(algorithm, self.queue[mid], node):
        lower = mid + 1
      elif self.lessThanNode(algorithm, node, self.queue[mid]):
        higher = mid - 1
      else:
        break
    return mid+1

  def printNodeValue(self, algorithm, node):
    if algorithm == algorithmTypes["breadth"]:
      return str(node.depth)
    elif algorithm == algorithmTypes["depth"]:
      return str(-node.depth)
    elif algorithm == algorithmTypes["depth_limited"]:
      return str(-node.depth)
    elif algorithm == algorithmTypes["iterative_deepening"]:
      return str(-node.depth)
    elif algorithm == algorithmTypes["uniform"]:
      return str(node.cost)
    elif algorithm == algorithmTypes["greedy"]:
      return str(node.heuristic)
    elif algorithm == algorithmTypes["A*"]:
      return str(node.cost + node.heuristic)

  def search(self, newTransitions, algorithm, heuristic=0, limit=-1):
    totalNodesVisited = 0
    while True:
      if not self.queue:
        print("No solution found!")
        return (None, totalNodesVisited)

      currentNode = self.queue.pop(0)
      totalNodesVisited += 1
      currentState = currentNode.state

      if self.checkVisited: 
        self.visited.append(str(currentState))
      
      if self.isFinalState(currentState):
        break
      
      if (algorithm == algorithmTypes["depth_limited"] and currentNode.depth >= limit): 
        continue
      currTransitions = newTransitions(currentNode, heuristic)
      if self.checkVisited:
        currTransitions = list(filter(lambda transition : str(transition.state) not in self.visited, currTransitions))

      for transition in currTransitions:
        self.queue.insert(self.getInsertPosition(algorithm, transition), transition)

    
    path = self.getPath(currentNode)
    return (path, totalNodesVisited)


