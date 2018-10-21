from LinkedList.LinkedList import LinkedList

def hasLoop(ll):
  slower_node = ll.head.next
  faster_node = ll.head.next.next

  while True:
    if slower_node is faster_node:
      return faster_node # Collision Node
    slower_node = slower_node.next
    if faster_node.next is None or faster_node.next.next is None:
      return False
    faster_node = faster_node.next.next

def detectLoop(ll):
  collision_node = hasLoop(ll)

  if not collision_node:
    return False
  
  start_node = ll.head
  start_node_2 = collision_node

  while True:
    if start_node.next is start_node_2.next:
      return start_node_2
    start_node = start_node.next
    start_node_2 = start_node_2.next


ll1 = LinkedList(['A', 'B', 'C', 'D', 'E', 'Q', 'W', 'E', 'R', 'T', 'Y'])
ll1.tail.next = ll1.head.next.next.next
ll1.tail = None

print(detectLoop(ll1))