class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=head
        while node.next!=None:
            if(node.val==node.next.val):
                node.next=node.next.next
            else:
                node=node.next
        return head
head=ListNode()
node=head
node.val=1
node.next=ListNode()
node=node.next
node.val=1
node.next=ListNode()
node=node.next
for i in range(1,5):
    node.val=i
    node.next=ListNode()
    node=node.next

head =Solution().deleteDuplicates(head)
while head.next!=None:
    print(head.val)
    head=head.next
