# Reverse Linked List (leetcode)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize dummy node
        dummy = ListNode(-1, None)
        # initialize curr node
        curr = head
        
        while curr:
            # keep current node (will be appended at the head)
            next_node = curr
						# move pointer
            curr = curr.next
            # swap process
            temp = dummy.next
            dummy.next = next_node
            next_node.next = temp
        
        return dummy.next