# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recursive(root):
            
            if not root:
                return 0
            
            maxLeft = 1 + recursive(root.left)
            maxRight = 1 + recursive(root.right)
            
            maxVal = max(maxLeft, maxRight)
            return maxVal
        
        return recursive(root)