# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.search(p,q)
    def search(self,p,q):
        if(p==None and q==None):
            return True
        if (p==None and not q==None) or ((not p==None) and q==None) or (not p.val==q.val):
            return False
        elif p.left==None and q.left==None:
            return self.search(p.right,q.right)
        elif p.right==None and q.right==None:
            return self.search(p.left,q.left)
        elif p.right==None and q.right==None and p.left==None and q.left==None:
            return True
        return self.search(p.left,q.left) and self.search(p.right,q.right)
    
from collections import deque

def create_tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values):
            node.left = TreeNode(values[index])
            queue.append(node.left)
            index += 1
        if index < len(values):
            node.right = TreeNode(values[index])
            queue.append(node.right)
            index += 1
    return root

def pre_order_traversal(node):
    if not node:
        return
    print(node.val, end=' ')
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

p = [0]
q = [0]

root_p = create_tree_from_list(p)
root_q = create_tree_from_list(q)

print(Solution().isSameTree(root_p,root_q))