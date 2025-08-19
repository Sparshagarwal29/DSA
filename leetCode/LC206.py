from typing import Optional
class Node:
    def __init__(self,val):
        self.val = val
        self.next: Optional[Node] = None

def reverseLinkedList(self,head):
    curr = head 
    prev = None 
    while curr is not None:
        front = curr.next 
        curr.next = prev
        prev = curr
        curr = front
    return prev