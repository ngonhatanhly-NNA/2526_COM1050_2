class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        temp = head
        length = 0
        
        while temp:
            temp = temp.next
            length += 1
        if length < n:
            return -1
        
        temp = head
        if length == n:
            head = temp.next
            return head

        prev = None
        for _ in range(1, length - n + 1):
            prev = temp
            temp = temp.next

        prev.next = temp.next

        return head