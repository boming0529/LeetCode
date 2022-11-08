# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head):
        ''' time compli'''
        
        if head is None:
            return head
        
        pre, current, ans = None, head, head.next
        
        
        while current is not None and current.next is not None:
            temp = current.next
            current.next = temp.next
            temp.next = current
            if pre is not None:
                pre.next = temp
            pre = current
            current = pre.next or None
        return ans or head