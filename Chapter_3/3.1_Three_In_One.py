class MyStack:
  def __init__(self):
    self.number_of_stacks = 3
    self.stack = []
    self.stack_sizes = [0] * 3

  def push(self, stack_number, value):
    index_before_insert = 0
    for i in range(stack_number + 1):
      index_before_insert += self.stack_sizes[i]

    self.stack = self.stack[:index_before_insert] + [value] + self.stack[index_before_insert:]
    self.stack_sizes[stack_number] += 1

  def pop(self, stack_number):
    if self.isEmpty(stack_number):
      raise Exception('Size is empty!')

    index_remove = -1
    for i in range(stack_number + 1):
      index_remove += self.stack_sizes[i]
  
    value = self.stack[index_remove]
    index_after_remove = index_remove + 1
    self.stack = self.stack[:index_remove]  + self.stack[index_after_remove:]
    self.stack_sizes[stack_number] -= 1

    return value

  def peek(self, stack_number):
    if self.isEmpty(stack_number):
      raise Exception('Size is empty!')

    index = -1
    for i in range(stack_number + 1):
      index += self.stack_sizes[i - 1]

    return self.stack[index]

  def isEmpty(self, stack_number):
    return self.stack_sizes[stack_number] == 0

stack = MyStack()
print(stack.isEmpty(1))
print(stack.push(0, 'A'))
print(stack.push(0, 'AA'))
print(stack.stack)
print(stack.push(1, 'B'))
print(stack.push(2, 'C'))
print(stack.peek(0))
print(stack.peek(1))
print(stack.peek(2))
print(stack.stack)
print('pop:', stack.pop(0))
print(stack.stack)
print(stack.peek(0))
print(stack.peek(1))
print(stack.peek(2))
print('pop:', stack.pop(1))
print('pop:', stack.pop(2))
print(stack.peek(0))
print(stack.stack)
print('pop:', stack.pop(0))
print(stack.stack)