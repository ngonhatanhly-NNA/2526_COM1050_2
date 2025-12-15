from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None or head == right:
            return head
        curr, prev = head, None
        
        while left > 1:
            left -= 1
            right -= 1
            
            prev = curr
            curr = curr.next
            # i to left, mean curr to the beginning of left    
        # Record so after, we can link 
        tail, first = curr,  prev
        while right > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

            right -= 1

        if first:
            first.next = prev
            
        else:
            head = prev
        tail.next = curr
            
        return head
            