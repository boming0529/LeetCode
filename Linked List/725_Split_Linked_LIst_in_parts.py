# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head, k):
        hashmap = {}
        cur = head
        count = 0
        while cur:
            count += 1
            hashmap[count] = cur
            cur = cur.next

        n = 1 if count<k else count//k
        otherwise = 0 if count<k else count % k

        ans = []
        other = 0
        for index in range(1,k+1):
            fisrt = n * index - (n - 1) + other
            other += 1 if otherwise >= index and otherwise != 0 else 0
            tail = (n * index) + other
            if tail == 0:
                ans.append(None)
            else: 
                ans.append(hashmap.get(fisrt, None))
            if hashmap.get(tail, None):
                hashmap.get(tail).next = None
          
        return ans