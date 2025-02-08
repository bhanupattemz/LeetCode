# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a=0
        p=headA
        q=headB
        q.next=p
        self.search(headA,headB)
        def search(self,headA,headB){
            if (headA.next!=None or headB.next!=None) and (headA.next.val==headB.next.val):
                return (headA,headB)
        }