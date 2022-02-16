# Remove N-th Node from End of List

# Sentinel Node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set dummy node previous to the head (sentinel node)
        dummy = ListNode(-1, head)
        
        # set early stopping node
        stopper = dummy
        
        # move stopper to n-th place in the Linked List
        for _ in range(n):
            stopper = stopper.next
        
        # initialize curr
        curr = dummy
        
        # find node previous to the target node (node being removed)
        while stopper.next:
            curr = curr.next
            stopper = stopper.next
        
        # remove target node
        curr.next = curr.next.next # (or stopper)
        
        return dummy.next
        
        
        