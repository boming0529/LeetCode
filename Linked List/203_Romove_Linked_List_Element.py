# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        if head is None: return head
        fast = head
        while fast:
            if head.val == val:
                head = head.next
            else:
                break
            fast = fast.next
        slow = ListNode(next=head)
        while fast:
            if fast.val == val:
                slow.next = slow.next.next
            else:
                slow = slow.next
            fast = fast.next
        return head
