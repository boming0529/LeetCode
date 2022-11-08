# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        ans = None
        while head:
            pre = head
            head = head.next
            pre.next = ans          
            ans = pre
        return ans
        