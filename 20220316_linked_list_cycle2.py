# Linked List Cycle

# fast and slow 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None
        
        slow = fast = head
        
        intersection = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                intersection = slow
                break
            
        if not intersection:
            return None
        
        check = intersection.next
        curr = head
        
        while curr != check:
            if check == slow:
                curr = curr.next
            
            check = check.next
            
        return curr
            
            
            
        