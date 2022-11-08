# -*- coding : utf-8 -*-
from operator import itemgetter


class Node(object):
    def __init__(self, val=0):
        self.__val = val
        self.__next = None

    def get_data(self):
        return self.__val
    
    def set_data(self, val):
        self.__val = val

    def get_next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next

class ListNode(object):
    def __init__(self, head=None):
        self.head = head
        self.__count = 0

    def insert(self, new_node):
        ''' time complexity : O(1) '''
        # set the next of the new node to the current head
        new_node.set_next(self.head)
        # set the head of the Linked list to the new head
        self.head = new_node
        # add 1 to the count
        self.__count += 1 

    def find(self, val):
        ''' time complexity : O(n) '''
        item = self.head
        while item != None:
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def remove(self, node):
        # ''' tiem complexity : O(n) '''
        # current = self.head
        # pre = None
        # while current is not None:
        #     if current.get_data() == item:
        #         break
        #     pre = current
        #     current = current.get_next()

        # run to last node
        # if current is None:
        #     raise ValueError(f'{item} is not in the list')
        # # remote first node 要改 head 指標
        # if pre is None:
        #     self.head = current.get_next()
        #     self.__count -= 1
        # else:
        #     pre.set_next(current.get_next())
        #     self.__count -= 1
        
        ''' tiem complexity : O(1) '''
        node.set_data(node.get_next().get_data())
        node.set_next(node.get_next().get_next())
        self.__count -= 1
        

    def get_count(self):
        return self.__count

    def is_empty(self):
        return self.head == None