# -*- coding : utf-8 -*-
from re import L
from ListNode import ListNode, Node


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

head = Node()
# head.set_next(node_1)
# node_1.set_next(node_2)
# node_2.set_next(node_3)
# print(node_1.get_next().get_data())

List = ListNode(None)
List.insert(node_1)
List.insert(node_2)
List.insert(node_3)
print(List.find(2))
print(List.get_count())
List.remove(node_2) 
print(List.find(2))



print(List.get_count())

k = 3
for i in range(1,k+1):
    print(i)

# LeetCode 804
s = set()
mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = 'hello'
print(words)
for w in words:                    
    m = ''
    for l in w: 
        print(l)
        print(ord(l))                      
        m += mos[ord(l) - ord('a')] 
    s.add(m)