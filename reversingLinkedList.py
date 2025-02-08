class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        list=[]
        while not head == None:
            list.append(head.val)
            head=head.next
        list.reverse()
        l=len(list)
        if l==0:
            return None
        head=ListNode()
        node=head
        for item in range(l):
            node.val=list[item]
            if not item == l-1:
                node.next=ListNode()
                node=node.next
        return head
print(Solution().reverseList())
        