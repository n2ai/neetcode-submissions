# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,nodeArray):
            if not node:
                return 0  # Return 0 as no nodes are processed in this path
            
            is_good = 0
            if not nodeArray or max(nodeArray) <= node.val:  # Check against the maximum of the array
                is_good = 1  # Current node is good
                nodeArray.append(node.val)  # Append current node value as it's a new maximum
            
            # Current node count as good or not, then explore children with a copy of the array
            return is_good + dfs(node.left, nodeArray[:]) + dfs(node.right, nodeArray[:])
        
        return dfs(root, [])

