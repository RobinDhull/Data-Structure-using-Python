#Q3.
class Node: 
	def __init__(self, value): 
		self.data = value 
		self.left = None
		self.right = None

def insertNode(node, data): 
	if (node == None): 
		return (Node(data))
	else:
		if (data <= node.data): 
			node.left = insertNode(node.left, data) 
		else: 
			node.right = insertNode(node.right, data) 
		return node 

def minValue(node): 
	current = node 
	while(current.left != None): 
		current = current.left 
	return current.data 
    
rootNode = None
rootNode = insertNode(rootNode,2) 
insertNode(rootNode,5) 
insertNode(rootNode,3) 
insertNode(rootNode,4) 
insertNode(rootNode,1) 
insertNode(rootNode,8) 

print(f"Minimum value in BST is {minValue(rootNode)}")
