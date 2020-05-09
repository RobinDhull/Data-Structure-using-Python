class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertFirst(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode


    def insertLast(self, value):
        newNode = Node(value)
        if (self.head == None):
            self.head = newNode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode     


    def insertInBetween(self, index, value):
        itemCount, count = 1, 0
        current = self.head
        while(current.next != None):
            itemCount += 1
            current = current.next
        if index > itemCount:
            print('Index out of range') 
        elif index == 0:
            self.insertFirst()
        else:
            current = self.head
            while(count < index-1):
                current = current.next
                count += 1
            newNode = Node(value)
            newNode.next = current.next 
            current.next = newNode

        
    def deleteFirst(self):
        current = self.head
        if (current == None):
            print('Linked List is empty')
        else:
            self.head = current.next


    def deleteEnd(self):
        current = self.head
        while(current.next != None):
            previous = current
            current = current.next
        previous.next = None

    
    def deleteWithValue(self, value):
        current = self.head
        if current != None and current.data == value:   
            self.head = current.next
            current = None
            return
        while (current.next != None):
            if (current.data == value):
                break
            previous = current
            current = current.next

        previous.next = current.next 
        current = None
        return

    
    def deleteAtPosition(self, index):
        count, total = 0, 0
        current = self.head
        while (current): 
            current = current.next
            total += 1
        current = self.head
        if index > total:
            print('Index out of range') 
        elif index == 0:
            self.head = current.next
            current = self.head
        else:
            current = self.head
            while(count != index):
                previous = current
                current = current.next
                count += 1
            previous.next = current.next

    def deleteAll(self):
        self.head = None
        return


    def viewList(self):
        if (self.head == None):
            print('Linked List is empty')
        else:
            current = self.head
            while(current != None):
                print(current.data)
                current = current.next


myList = LinkedList()
myList.insertLast(2)
myList.insertLast(5)
myList.insertLast(3)
myList.insertLast(8)
myList.viewList()
print("******************")
myList.insertInBetween(2,7)
myList.viewList()
print("******************")
#myList.deleteWithValue(7)
myList.deleteEnd()
#myList.deleteAll()
myList.viewList()



