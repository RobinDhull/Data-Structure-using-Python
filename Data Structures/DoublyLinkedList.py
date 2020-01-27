class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertFirst(self, value):
        newNode = Node(value)
        if (self.head == None):
            newNode.prev = None
            self.head = newNode
        else:
            currentNode = self.head
            while (currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode
            newNode.next = None
               
    def viewList(self):
        if (self.head == None):
            print('Doubly Linked List is empty')
        else:
            currentNode = self.head
            while (currentNode != None):
                print(currentNode.data)
                currentNode = currentNode.next
            
dllist = DoublyLinkedList()
dllist.insertFirst(5)
dllist.insertFirst(3)
dllist.insertFirst(8)
dllist.insertFirst(7)
dllist.viewList()
