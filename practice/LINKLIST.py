from typing import Optional
class Node:
    def __init__(self,val):
        self.val = val
        self.next: Optional[Node] = None

class singlyLinkedList:
    def __init__(self):
      self.head = None
    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def traverse(self):
        if self.head is None:
            print("empty linked list ")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr = curr.next
            print()
    # def insertAtPosition():


sll = singlyLinkedList()
sll.append(5)
sll.append(10)
sll.append(15)
sll.append(25)
sll.traverse()




