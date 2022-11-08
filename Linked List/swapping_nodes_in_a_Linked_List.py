# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k):

        hashmap = {}
        item = head
        count = 0
        while item:
            count += 1
            hashmap[count] = item
            item = item.next
        
        hashmap[k].val,hashmap[count-k+1].val = hashmap[count-k+1].val,hashmap[k].val

        return head
        