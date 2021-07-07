# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return None
        queue = []
        result = 0
        queue.append(root)
        
        while(len(queue) != 0):
            node = queue.pop(0)
            if node.val >= low and node.val <= high:
                result += node.val
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return result


            
