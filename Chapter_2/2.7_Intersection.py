from LinkedList.LinkedList import LinkedList

def Intersection(ll1, ll2):
  ll1_len = len(ll1)
  ll2_len = len(ll2)

  longer_node = ll1.head if ll1_len >= ll2_len else ll2.head
  shortter_node = ll2.head if ll2_len <= ll1_len else ll1.head

  len_diff = abs(ll1_len - ll2_len)

  if len_diff != 0:
    while len_diff != 0:
      longer_node = longer_node.next
      len_diff -= 1
  
  while longer_node.next != None:
    if longer_node == shortter_node:
      return longer_node
    
    longer_node = longer_node.next
    shortter_node = shortter_node.next

ll1 = LinkedList([3, 1, 5, 9, 7, 2, 1])

ll2 = LinkedList([4, 6])
ll2.tail.next = ll1.head.next.next.next.next
ll2.tail = ll1.tail

print(Intersection(ll1, ll2))


ll11 = LinkedList([3, 1, 5, 9, 7, 2, 1])
ll22 = LinkedList([5, 1, 5, 9, 7, 2, 1])

print(Intersection(ll11, ll22))
