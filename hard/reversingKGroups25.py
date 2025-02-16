class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def addlist(head,list):
            i=0
            node=head
            while i< len(list)-1:
                node.val=list[i]
                node.next=ListNode()
                node=node.next
                i+=1
            node.val=list[i]
            return node
        result=ListNode()
        node=result
        while head!=None:
            list=[]
            for i in range(k):
                if head==None:
                   addlist(node,list)
                   return result
                list.append(head.val)
                head=head.next
            list.reverse()
            node=addlist(node,list)
            if head!=None:
                node.next=ListNode()
                node=node.next
        return result


def convert_to_linked_list(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
        
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
lst = [1, 2, 3, 4, 5]
linkedList=convert_to_linked_list([1,2,3,4,5])
print_linked_list(linkedList)
head=Solution().reverseKGroup(linkedList,3)
print_linked_list(head)