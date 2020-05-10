class ArrayStack:
    def __init__(self, limit = 5):
        self.stack = [] * limit
        self.limit = limit
    
    def push(self, data):
        if self.isFull():
            return
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            return
        else:
            self.stack.pop()
        return

    def isFull(self):
        if len(self.stack) == self.limit:
            return
        
    def is_empty(self):
        if len(self.stack) == 0:
            return True

    def top(self):
        if len(self.stack) == 0:
            return
        self.stack[-1]

    def resize(self):
        self.limit = self.limit * 2
        newStack = ArrayStack(limit)
        newStack = self.stack
        self.stack = newStack
    
    def view(self):
        if self.is_empty():
            print('Stack is empty')
        while(len(self.stack) > 0):
            print(self.stack.pop())
        return
    
stack1 = ArrayStack(5)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.view()
stack1.pop()
print('**************')
stack1.view()
