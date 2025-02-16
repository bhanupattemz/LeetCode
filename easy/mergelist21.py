
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result=ListNode()
        head=result
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                result.next=ListNode(list1.val,None)
                result=result.next
                list1=list1.next
            else:
                result.next=ListNode(list2.val,None)
                result=result.next
                list2=list2.next
        def app_rem(list,result):  
            while list!=None: 
                  result.next=ListNode(list.val)
                  result=result.next
                  list=list.next
        app_rem(list1,result) 
        app_rem(list2,result)
        
        return head.next
    
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

list1=list_to_linked_list([0,1,2,3])
list2=list_to_linked_list([-100,1,2,4])


print(Solution().mergeTwoLists(list1,list2).val)