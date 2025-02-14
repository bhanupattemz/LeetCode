# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=head
        l=0
        while node:
            l+=1
            node=node.next
        n=l-n+1
        node=head
        i=0
        prev=None
        while node:
            i+=1
            if(i==n):
                if(node.next):
                    if(prev):
                        prev.next=node.next
                    else:
                        head=head.next
                elif prev :
                    prev.next=None
                else:
                    return None
                break
            prev=node
            node=node.next
        return head

