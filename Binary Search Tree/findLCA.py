#Q7.
class Node:
	def __init__(self, value): 
		self.data = value 
		self.left = None
		self.right = None

def LCA(root, n1, n2): 
	while (root != None):
		if (root.data > n1 and root.data > n2): 
			root = root.left 
		elif (root.data < n1 and root.data < n2): 
			root = root.right 
		else: 
			break
	return root

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 

n1 = 10, n2 = 14
res = LCA(root, n1, n2) 
print(f"Lowest Common Ancestor of {n1} and {n2} is {res.data}") 
n1 = 14, n2 = 8
res = LCA(root, n1, n2) 
print(f"Lowest Common Ancestor of {n1} and {n2} is {res.data}")
n1 = 10, n2 = 22
res = LCA(root, n1, n2) 
print(f"Lowest Common Ancestor of {n1} and {n2} is {res.data}") 
