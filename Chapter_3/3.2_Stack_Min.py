class StackMin:
  def __init__(self):
    self.stack = []
    self.mins = []

  def push(self, value):
    if len(self.mins) > 0:
      if self.mins[-1] >= value:
        self.mins.insert(len(self.mins), self.mins[-1])
      else:
        self.mins.insert(len(self.mins), value)
    else:
      self.mins.insert(len(self.mins), value)
    self.stack.insert(len(self.stack), value)

  def pop(self):
    if len(self.stack) == 0:
      return

    self.mins.pop()
    return self.stack.pop()

  def mini(self):
    if len(self.stack) == 0:
      return None
    return self.mins[-1]


stack = StackMin()
stack.push(6)
stack.push(1)
stack.push(4)
stack.push(10)
stack.push(7)
print(stack.mini()) # 10
stack.pop()
stack.pop()
print(stack.mini()) # 6
