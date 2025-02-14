# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        def path(node,result):
            if not (node.left or node.right):
                return result
            current=result.pop()
            if(node.left):
                result.append(f'{current}->{node.left.val}')
                path(node.left,result)
            if(node.right):
                result.append(f'{current}->{node.right.val}')
                path(node.right,result)
            return result
        return path(root,[f'{root.val}'])
    