# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        collection = []
        
        def inorder(node):
            if node == None:
                return
            else:
                inorder(node.left)
                collection.append(node.val)
                inorder(node.right)
        
        inorder(root)
        return collection
