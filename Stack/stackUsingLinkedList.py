class Node:
    def __Self__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        
    def view(self):
        if self.head == None:
            print('Stack is empty')
        else:
            temp = self.head
            while (temp.next):
                print(temp.data)
                temp = temp.next

stack = Stack()
stack.push(1)
stack.view()