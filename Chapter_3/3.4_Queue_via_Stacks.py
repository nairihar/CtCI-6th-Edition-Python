from utils.stack import Stack


class QueueViaStacks:

    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def __processStacks(self):
        if self.second_stack.isEmpty():
            while not self.first_stack.isEmpty():
                item = self.first_stack.pop()
                self.second_stack.push(item)

    def push(self, item):
        self.__processStacks()
        self.first_stack.push(item)
  
    def pop(self):
        self.__processStacks()
        return self.second_stack.pop()


qvs = QueueViaStacks()
qvs.push(1)
qvs.push(2)

print('should be 1', qvs.pop())
print('should be 2', qvs.pop())
