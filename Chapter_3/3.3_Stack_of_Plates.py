from utils.stack import Stack

class StackOfStacks:
  def __init__(self):
    self.__stack_size = 3

    self.stack = self.__new_stack()
    self.stacks = [self.stack]
  
  def push(self, v):
    self.__check_and_add_stack()
    self.stack.push(v)
    return self.stack
  
  def pop(self):
    self.__check_and_remove_stack()
    v = self.stack.pop()
    return v
  
  def peek(self):
    return self.stack.peek()
  
  def popAt(self, index):
    if len(self.stacks) >= index + 1:
      return self.stacks[index].pop()
  
  def __new_stack(self):
    return Stack(self.__stack_size)
  
  def __check_and_add_stack(self):
    if self.stack.size() == self.__stack_size:
      self.stack = self.__new_stack()
      self.stacks.insert(len(self.stacks), self.stack)

  def __check_and_remove_stack(self):
    if self.stack.size() == 0:
      self.stacks.pop()
      if len(self.stacks) > 0:
        self.stack = self.stacks[-1]
      else:
        self.stack = self.__new_stack()
        self.stacks.insert(len(self.stacks), self.stack)


stack = StackOfStacks()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.stack.getFullArray())
stack.pop()
print(stack.stack.getFullArray())
print(stack.stacks[0].getFullArray())
stack.pop()
print(stack.stack.getFullArray())