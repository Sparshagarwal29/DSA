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
    def insertAtPosition(self,val,positon):
        new_node = Node(val)
        if positon == 0 :
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < positon:
                prev_node = current
                current = current.next
                count +=1
            prev_node.next = new_node # type: ignore
            new_node.next = current
    def deleteNode(self,val):
        temp = self.head
        if temp.next is not None: # type: ignore
            if temp.val == val: # type: ignore
                self.head == temp.next # type: ignore
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next # type: ignore
                    return
                else:
                    print("node not found")





sll = singlyLinkedList()
sll.append(5)
sll.append(10)
sll.append(15)
sll.append(25)
sll.traverse()




