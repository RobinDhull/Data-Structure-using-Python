class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = Node(value)
        if (self.head == None):
            self.head = newNode
        else:
            currentNode = self.head
            while (currentNode.nextNode != None):
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode
    
    def reverseList(self):
        previousNode = None
        currentNode = self.head
        while (currentNode != None):
            next = currentNode.nextNode
            currentNode.nextNode = previousNode 
            previousNode = currentNode 
            currentNode = next
        self.head = previousNode
    
    def printList(self):
        currentNode = self.head 
        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.nextNode

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.printList()
print("***********")
llist.reverseList()
llist.printList()