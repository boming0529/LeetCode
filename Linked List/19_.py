# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(next=head)
        
        hashmap = {}
        index = 0
        hashmap[index] = dummy
        item = head
        while item:
            index += 1
            hashmap[index] = item
            item = item.next
        
        hashmap[index].next = None
        hashmap[index-n].next, hashmap[index-n+1].next = hashmap[index-n].next.next, None
        return head if (index - n) != 0 else hashmap[index-n].next

class Soulution2:
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        
        if not fast: return fast.next

        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head