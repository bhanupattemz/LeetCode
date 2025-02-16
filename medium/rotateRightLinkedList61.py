# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node=head
        l=1
        if not (node):
            return None
        while node.next:
            node=node.next
            l+=1
        k=k%l
        n=l-k
        i=0
        ptr=head
        while ptr:
            i+=1
            if(i==n):
                node.next=head
                head=ptr.next
                ptr.next=None
                return head
            ptr=ptr.next

        return head