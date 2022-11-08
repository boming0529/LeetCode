# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None: return None
        
        group1 = ListNode(0)
        odd = group1
        group2 = ListNode(0)
        even = group2
        
        count = 1
        
        while head:
            if count % 2 == 1: # odd
                odd.next = ListNode(head.val)
                odd = odd.next
            else:
                even.next = ListNode(head.val)
                even = even.next 
            head, count = head.next, count + 1

        odd.next = group2.next
        return group1.next
        
class Solution2:
    def oddEvenList(self, head):
        '''  '''
        if head is None: return None
        
        odd, even, con = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = odd.next
        odd.next = con
        return head