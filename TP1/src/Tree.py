class Node:
  def __init__(self, state, depth, cost, heuristic, parent):
    self.state = state
    self.depth = depth
    self.cost = cost
    self.heuristic = heuristic
    self.parent = parent
  
  def __str__(self):
    return str(self.state)