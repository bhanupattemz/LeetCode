# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(level,node):
            if not node :
                return level
            return max(depth(level+1,node.left),depth(level+1,node.right))
           
        return depth(0,root)
        