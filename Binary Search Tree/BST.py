class Node: 
	def __init__(self, value): 
		self.left = None
		self.right = None
		self.val =  value 

def insert(root, node): 
	if (root == None): 
		root = node 
	else: 
		if (root.val < node.val): 
			if (root.right == None): 
				root.right = node 
			else: 
				insert(root.right, node) 
		else: 
			if (root.left == None): 
				root.left = node 
			else: 
				insert(root.left, node) 
 
def inorderTraversal(root): 
	if (root != None): 
		inorderTraversal(root.left) 
		print(root.val) 
		inorderTraversal(root.right)

def Search(root, value):  
    if (root == None):
        print(root)
        return
    elif (root.val == value): 
        print(root.val, 'Found')
        return
    elif (root.val < value): 
        return Search(root.right, value)

    return Search(root.left, value)  

list_ = ['P', 'V', 'S', 'C', 'M', 'Y']
r = Node('A')
for i in list_:
    insert(r,Node(i))

Search(r, 'D')
