class Node:
	def __init__(self, value): 
		self.value = value 
		self.left = None
		self.right = None

def inOrderTraversal(root): 
	if (root != None): 
		inOrderTraversal(root.left) 
		print (root.value, inOrderTraversal(root.right))

def insertNode(node, value): 
	if (node == None): 
		return Node(value) 
	elif (value < node.value): 
		node.left = insertNode(node.left, value) 
	else: 
		node.right = insertNode(node.right, value) 
	return node

def minValueNode( node): 
	current = node
	while (current.left != None):
		current = current.left 
	return current 

def deleteNode(root, value):
	if (root == None): 
		return root 
	elif (value < root.value): 
		root.left = deleteNode(root.left, value)
	elif(value > root.value): 
		root.right = deleteNode(root.right, value) 
	else: 
		if (root.left == None): 
			temp = root.right 
			root = None
			return temp 
		elif (root.right == None): 
			temp = root.left 
			root = None
			return temp 

		temp = minValueNode(root.right)
		root.value = temp.value
		root.right = deleteNode(root.right , temp.value)
	return root

root = None
root = insertNode(root, 10) 
root = insertNode(root, 20) 
root = insertNode(root, 30) 
root = insertNode(root, 40) 
root = insertNode(root, 50) 
root = insertNode(root, 60) 
root = insertNode(root, 70) 

print("***************Inorder traversal of the given tree*******************")
inOrderTraversal(root) 

print("Delete 30")
root = deleteNode(root, 30) 
print("***************Inorder traversal of the modified tree****************")
inOrderTraversal(root)
