#Q4.
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def findInorderPS(root, val, list1, list2): 
	if(root == None): 
		return
	findInorderPS(root.left, val, list1, list2) 
	
	if(root and root.data > val): 
		if((not list2[0]) or list2[0] and list2[0].data > root.data): 
			list2[0] = root 
	elif(root and root.data < val): 
		list1[0] = root 
	findInorderPS(root.right, val, list1, list2) 

rootNode = Node(10) 
rootNode.left = Node(20) 
rootNode.right = Node(30) 
rootNode.left.left = Node(40) 
rootNode.left.right = Node(50) 
rootNode.right.left = Node(60) 
rootNode.right.right = Node(70) 
list1 = [None] 
list2 = [None] 
	
findInorderPS(rootNode, 50, list1, list2) 

if(list1[0] != None): 
	print(list1[0].data, end = "") 
if(list2[0] != None): 
	print("", list2[0].data)