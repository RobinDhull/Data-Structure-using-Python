class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.start = None

    def push(self, value):
        newNode = Node(value)
        if (self.start == None):
            self.start = newNode
        else:
            currentNode = self.start
            while (currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = newNode
    
    def reverseList(self):
        previous = None
        head = self.start
        currentNode = None
        while (head):
            currentNode = head.next
            head.next = previous
            previous = head
            head = currentNode
        self.start = previous
    
    def printList(self):
        currentNode = self.start 
        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.printList()
print("***********")
llist.reverseList()
llist.printList()