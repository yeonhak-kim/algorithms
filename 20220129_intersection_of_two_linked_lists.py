# Intersection of Two Linked Lists (leetcode)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # initialize length variables
        a_length = b_length = 0
        
        # initialize pointers for listA and listB
        curr_a, curr_b = headA, headB
        
        # PART 1: compute lengths of listA and listB
        while curr_a or curr_b:
            if curr_a:
                a_length += 1
                curr_a = curr_a.next
            
            if curr_b:
                b_length += 1
                curr_b = curr_b.next 
                
        # length difference
        length_diff = abs(a_length - b_length)
        
        # re-initialize pointers for listA and listB
        curr_a, curr_b = headA, headB
        
        # PART 2: align two pointers
        counter = 0
        if a_length > b_length:
            while counter < length_diff:
                curr_a = curr_a.next
                counter += 1
        else:
            while counter < length_diff:
                curr_b = curr_b.next
                counter += 1
        
        # initialize intersection variable
        intersection = None
        
        # PART 3: find intersection between listA and listB
        while curr_a and curr_b:
            if curr_a == curr_b:
                intersection = curr_a
                break
            
            curr_a = curr_a.next 
            curr_b = curr_b.next
        
        return intersection