# Python3 program to check if
# all three given traversals
# are of the same tree
class node:

	def __init__(self, x):
	
		self.data = x
		self.left = None
		self.right = None

preIndex = 0

# Function to find index of value
# in arr[start...end]. The function
# assumes that value is present in in
def search(arr, strt, end, value):

	for i in range(strt, end + 1):
		if(arr[i] == value):
			return i

# Recursive function to construct
# binary tree of size lenn from
# Inorder traversal in[] and Preorder
# traversal pre[]. Initial values
# of inStrt and inEnd should be 0
# and lenn - 1. The function doesn't
# do any error checking for cases
# where inorder and preorder do not
# form a tree
def buildTree(inn, pre, inStrt, inEnd):

	global preIndex

	if(inStrt > inEnd):
		return None

	# Pick current node from Preorder
	# traversal using preIndex and
	# increment preIndex
	tNode = node(pre[preIndex])
	preIndex += 1

	# If this node has no children
	# then return
	if (inStrt == inEnd):
		return tNode

	# Else find the index of this
	# node in Inorder traversal
	inIndex = search(inn, inStrt, inEnd, tNode.data)

	# Using index in Inorder traversal,
	# construct left and right subtress
	tNode.left = buildTree(inn, pre, inStrt, inIndex - 1)
	tNode.right = buildTree(inn, pre, inIndex + 1, inEnd)

	return tNode

# function to compare Postorder traversal
# on constructed tree and given Postorder
def checkPostorder(node, postOrder, index):
	if (node == None):
		return index

	# first recur on left child
	index = checkPostorder(node.left, postOrder, index)

    # now recur on right child
    index = checkPostorder(node.right, postOrder, index)

	# Compare if data at current index in
	# both Postorder traversals are same
	if (node.data == postOrder[index]):
		index += 1
	else:
		return - 1

	return index

# Driver code
if __name__ == '__main__':

	inOrder = [4, 2, 5, 1, 3]
	preOrder = [1, 2, 4, 5, 3]
	postOrder = [4, 5, 2, 3, 1]
	lenn = len(inOrder)

	# build tree from given
	# Inorder and Preorder traversals
	root = buildTree(inOrder, preOrder,
					0, lenn - 1)

	# compare postorder traversal on
	# constructed tree with given
	# Postorder traversal
	index = checkPostorder(root, postOrder, 0)

	# If both postorder traversals are same
	if (index == lenn):
		print("Yes")
	else:
		print("No")


