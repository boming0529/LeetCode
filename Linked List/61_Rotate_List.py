# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head,  k: int, n: int = 0):
        if head is None : return None

        fast, slow = head, None
        while fast and k:
            n += 1
            slow = fast
            fast = fast.next
            k = k -1

        if k == 0:
            if not slow or not slow.next:
                return head
            tail = ListNode(next=head)
            while slow.next:
                tail = tail.next
                slow = slow.next
            slow.next = head
            ans = tail.next
            tail.next = None
            return ans
        else:
            k = k % n
            return self.rotateRight(head, k, n)
        
            
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''https://leetcode.com/problems/rotate-list/discuss/1838907/Python-or-VISUAL-or-Easy-to-Understand-or-O(N)-Time-or-O(1)-Space'''
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer
        