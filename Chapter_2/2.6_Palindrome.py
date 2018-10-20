from math import floor
from LinkedList.LinkedList import LinkedList

def checkPalindrome(ll):
  ll_len = len(ll)
  half_count = floor(ll_len/2)
  len_is_even = ll_len%2 == 0
  half_reverse_ll = LinkedList()

  current = ll.head
  for i, value in enumerate(ll):
    if half_count < i + 1:
      break
    half_reverse_ll.add_to_beginning(str(value))
    current = current.next
  
  if not len_is_even:
    current = current.next
  
  current_from_half = half_reverse_ll.head
  while current:
    if str(current_from_half.value) != str(current.value):
      return False
    current_from_half = current_from_half.next
    current = current.next

  return True


ll = LinkedList(['l', 'e', 'v', 'e', 'l'])
print(checkPalindrome(ll))

ll = LinkedList(['l', 'e', 'e', 'l'])
print(checkPalindrome(ll))

ll = LinkedList(['l', 'e', 'v', 'a', 'l'])
print(checkPalindrome(ll))