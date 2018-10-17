from LinkedList.Node import Node

def partition(node, n):
  prev_main_node = node
  next_main_node = node

  node = node.getNext()

  while node != None:
    v = node.getValue()
    next_node = node.getNext()

    if v < n:
      prev_main_node.setPrev(node)
      node.setNext(prev_main_node)
      node.setPrev(None)
      prev_main_node = node
    else:
      next_main_node.setNext(node)
      node.setPrev(next_main_node)
      next_main_node = node

    node = next_node
  
  return prev_main_node


node = Node(1)
node.connect(2).connect(10).connect(3).connect(4).connect(5)

new_node = partition(node, 5)

print(new_node.getPrev())
print(new_node.getValue())
print(new_node.getNext().getValue())
print(new_node.getNext().getNext().getValue())
print(new_node.getNext().getNext().getNext().getValue())
print(new_node.getNext().getNext().getNext().getNext().getValue())
print(new_node.getNext().getNext().getNext().getNext().getNext().getValue())
print(new_node.getNext().getNext().getNext().getNext().getNext().getNext())

