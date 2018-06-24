# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = l1
        count = 0
        
        while l1 is not None and l2 is not None:
            l1.val = l1.val + l2.val + count
            count = 0
            if l1.val >= 10:
                count = 1
                l1.val = l1.val - 10
            
            if l1.next is None and l2.next is not None:
                l1.next = ListNode(0)
            if l1.next is not None and l2.next is None:
                l2.next = ListNode(0)
            if l1.next is None and l2.next is None and count == 1:
                l1.next = ListNode(1)
            
            l1 = l1.next
            l2 = l2.next
                
        return head