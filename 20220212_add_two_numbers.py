# Add Two Numbers (leetcode)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        hasCarry = False
        dummy = ListNode(-1, None)
        curr = dummy
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            hasOverflow, sum_val = divmod(val1 + val2 + 1, 10) if hasCarry else divmod(val1 + val2, 10)
            hasCarry = True if hasOverflow else False
            
            newNode = ListNode(sum_val, None)
            curr.next = newNode
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None            
        if hasCarry:
            curr.next = ListNode(1, None)
        
        return dummy.next
            
            