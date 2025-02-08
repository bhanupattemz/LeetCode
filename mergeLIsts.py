
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def print_list(current):
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("\n")
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head=ListNode()
  
        def merge(head,list):
            node=head
            result=ListNode()
            dup=result
            while node and list:
                if list.val> node.val :
                    result.val=node.val
                    node=node.next
                else:
                    result.val=list.val
                    list=list.next
                if node and list:
                    result.next=ListNode()
                    result=result.next
            result.next=node if node  else list
            return dup
        if len(lists)==1:
            return lists[0]
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(merge(l1, l2))
            lists = mergedLists
        return lists[0] if lists else None
    

def list_to_linked_list(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

    
current =Solution().mergeKLists([list_to_linked_list([2]),list_to_linked_list([-1])])
print_list(current)