# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root) -> int:
        if(not root):
            return 0
        def count(node):
            if(not node):
                return 0
            c=0
            if(node.left):
                c+=count(node.left)+1
            if(node.right):
                c+=count(node.right)+1
            return c
        return count(root)+1

        