class Node:
    def __init__(self, data):
        self.data = data
        self.previousNode = None
        self.nextNode = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertFirst(self, value):
        newNode = Node(value)
        if (self.head == None):
            newNode.previousNode = None
            self.head = newNode
        currentNode = self.head
        newNode.nextNode = currentNode
        newNode.previousNode = None
        

    def insertLast(self, value):
        newNode = Node(value)
        if (self.head == None):
            newNode.previousNode = None
            self.head = newNode
        currentNode = self.head
        while (currentNode.nextNode != None):
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode
        newNode.previousNode = currentNode
        newNode.nextNode = None
        return   

    
    def deleteLast(self):
        if (self.head == None):
            return
        currentNode = self.head
        while (currentNode.nextNode != None):
            previousNode = currentNode
            currentNode = currentNode.nextNode
        previousNode.nextNode = None

    
    def deleteWithValue(self, target):
        if (self.head == None):
            return
        currentNode = self.head
        while (currentNode.nextNode != None):
            if (currentNode.nextNode.data == target):
                previousNode = currentNode
                currentNode.nextNode = None
                previousNode.nextNode = currentNode.nextNode
                return
            currentNode = currentNode.nextNode
        return


    def viewList(self):
        if (self.head == None):
            print('Doubly Linked List is empty')
        else:
            currentNode = self.head
            while (currentNode != None):
                print(currentNode.data)
                currentNode = currentNode.nextNode
            
dllist = DoublyLinkedList()
dllist.insertFirst(5)
dllist.insertFirst(3)
dllist.insertFirst(8)
dllist.insertFirst(7)
dllist.viewList()
print('****************')
#dllist.deleteLast()
#dllist.viewList()
#print('****************')
#dllist.deleteWithValue(5)
#dllist.viewList()
