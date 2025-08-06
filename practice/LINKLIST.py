from typing import Optional
class Node:
    def __init__(self,val):
        self.val = val
        self.next: Optional[Node] = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)
node5 = Node(25)


node2.next = node3
node1.next = node2 
node3.next = node4
node4.next = node5


print(node1.val)
print(node1.next.val) 