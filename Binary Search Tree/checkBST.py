class Node: 
    def __init__(self, value):  
        self.data = value 
        self.left = None
        self.right = None
  
def isBST(root, left = None, right = None):  
    if (root == None) : 
        return True
    if (left != None and root.data <= left.data) : 
        return False
    if (right != None and root.data >= right.data) : 
        return False
   
    return isBST(root.left, left, root) and isBST(root.right, root, right) 

root = Node(1) 
root.left = Node(3) 
root.right = Node(8) 
root.left.left = Node(2) 
root.left.right = Node(5) 

if (isBST(root)): 
	print("Given Tree is a BST")
else: 
	print("Given Tree is not a BST")
