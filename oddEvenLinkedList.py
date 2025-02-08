class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even=ListNode()
        odd=ListNode()
        node1=odd
        node2=even
        while not head==None:
            if head.val%2==0:
                node2.next=ListNode()
                node2=node2.next
                node2.val=head.val
            else:
                node1.next=ListNode()
                node1=node1.next
                node1.val=head.val 
            head=head.next
        node1.next=even
        return node1.next
                
            
        