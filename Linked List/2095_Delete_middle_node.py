# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def deleteMiddle(self, head):
        
        hashmap = {}
        item = head
        count = 0
        while item:
            count += 1
            hashmap[count] = item
            item = item.next
        
        middle = count//2
        if count == 1 : return None
        
        hashmap[middle].next = hashmap[middle].next.next
        
        return head

class Solution2:
    def deleteMiddle(self, head):
        ''' using Fast and Slow Pointers.'''
        if head.next == None: return None
        fast, slow = head.next.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head