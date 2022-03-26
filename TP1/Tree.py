class Node:
  def __init__(self, value, prev):
    self.value = value
    self.prev = prev
  
  def __str__(self):
    return str(self.value)