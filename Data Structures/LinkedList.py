class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertLast(self, value):
        newNode = Node(value)
        if (self.head == None):
            self.head = newNode
        else:
            currentNode = self.head
            while (currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = newNode
        
    def viewList(self):
        if (self.head == None):
            print('Linked List is empty')
        else:
            currentNode = self.head
            while(currentNode != None):
                print(currentNode.data)
                currentNode = currentNode.next

    def deleteFirst(self):
        currentNode = self.head
        if (currentNode == None):
            print('Linked List is empty')
        else:
            currentNode = currentNode.next
    
    def insertFirst(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode     

    def insertInBetween(self, index, value):
        itemCount, count = 1, 0
        currentNode = self.head
        while(currentNode.next != None):
            itemCount += 1
            currentNode = currentNode.next
        if index > itemCount:
            print('Index out of range')
        elif index == 0:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
        else:
            currentNode = self.head
            while(count != index-1):
                currentNode = currentNode.next
                count += 1
            newNode = Node(value)
            newNode.next = currentNode.next 
            currentNode.next = newNode

myList = LinkedList()
myList.insertLast(2)
myList.insertLast(5)
myList.insertLast(3)
myList.insertLast(8)
myList.viewList()
print("******************")
myList.insertInBetween(2,7)
myList.viewList()


