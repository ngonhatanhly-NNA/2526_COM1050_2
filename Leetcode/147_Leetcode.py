from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = head

        while curr:
            temp = curr.next
            prev = dummy
            
            while prev.next and prev.next.val < curr.val:
                prev =prev.next
            # Curr chi toi none, or cycle
            curr.next =  prev.next
            # dummy to curr
            prev.next = curr

            curr = temp

        return dummy.next