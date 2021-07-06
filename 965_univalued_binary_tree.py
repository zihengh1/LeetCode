# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        collection = []
        
        def dfs(node):
            if node != None:
                collection.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        if len(set(collection)) == 1:
            return True
        else:
            return False
