class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = Node(value)
        if (self.head == None):
            self.head = newNode
        else:
            currentNode = self.head
            while (currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = newNode
        currentNode = self.head
    
    def viewLinkedList(self):
        count = 1
        currentNode = self.head
        while (currentNode != None):
            print("Node {} is".format(count), currentNode.data)
            currentNode = currentNode.next
            count += 1

    def hasCycle(self):
        head = self.head
        if head == None:
            return 'Cycle Not Present'
        fast = head.next
        slow = head

        while fast is not None and slow is not None and fast.next is not None:
            if fast == slow:
                return 'Cycle Present'
            fast = fast.next.next
            slow = slow.next
        return 'Cycle Not Present'
            
    
linkedlist = LinkedList()
linkedlist.push(2)
linkedlist.push(5)
linkedlist.push(3)
linkedlist.push(7)
linkedlist.head.next.next.next.next = linkedlist.head.next
print(linkedlist.hasCycle())

