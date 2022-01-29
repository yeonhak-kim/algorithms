# Linked List Cycle (leetcode)

# Slow and Fast Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # no cycle for NULL
        if not head: return False
        
        # initialize slow and fast pointer
        slow, fast = head, head.next
        
        while fast:
            # end to list exists
            if not fast.next:
                return False
            # cycle found
            if slow == fast:
                return True
            
            fast = fast.next.next
            slow = slow.next
        
        return False