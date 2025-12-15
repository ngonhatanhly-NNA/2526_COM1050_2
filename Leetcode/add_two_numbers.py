
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        # Create a newpointer to store
        remainder = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or remainder > 0:
            newVal = remainder
            if l1:
                newVal += l1.val
                l1 = l1.next
            if l2:
                newVal += l2.val
                l2 = l2.next
            
            remainder = newVal // 10
            newVal %= 10

            newNode = ListNode(newVal)
            curr.next = newNode
            curr = newNode

        return dummy.next