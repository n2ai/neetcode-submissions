# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(root):
            nonlocal d
            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeigh = dfs(root.right)
            dia = leftHeight + rightHeigh
            d = max(d, dia)

            return 1 + max(leftHeight, rightHeigh)
        dfs(root)
        return d