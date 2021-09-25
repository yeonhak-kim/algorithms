# Remove Nth Node from End of List
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = fast = dummy = ListNode(0, head)
    
    if not slow.next:
        return None
    
    for i in range(n + 1):
        fast = fast.next
    
    while fast:
        slow = slow.next 
        fast = fast.next 
    
    temp = slow.next.next
    slow.next  = temp
    
    return dummy.next