class Node:
    def __init__(self,val) -> None:
        self.val = val 
        self.next: Node | None = None
        self.prev: Node | None = None

class DoublyLinkedList:
    def __init__(self) -> None:
       self.head: Node | None = None
# insert at Head  --> Time complexity O(1) and Space complexity O(1)
    def insertAtHead(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode 
        else:
            newNode.next = self.head 
            self.head.prev = newNode
            self.head = newNode
# insert at the last (tail)(apeend) --> Time complexity O(n) and Space complexity O(1)
    def apeend(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head 
            while curr.next is not None:
                curr = curr.next 
            curr.next = newNode
            newNode.prev = curr
# insert at the given position --> Time complexity O(n) and Space complexity O(1)
    def insertAtpposition(self,val,position):
        newNode = Node(val)
        if position == 0:
            self.insertAtHead(val)
            return
        curr = self.head
        count = 0 
        while curr and count < position - 1 :
            curr = curr.next 
            count += 1
        if curr is None:
            print("Position out of bounds")
            return
        newNode.next = curr.next 
        newNode.prev = curr

        if curr.next:
            curr.next.prev = newNode
        curr.next = newNode 
# traversal --> Time complexity O(n) and Space complexity O(1)
    def traversal(self):
        if self.head is None:
            print("Empty list")
            return
        else:
            curr = self.head
            while curr:
                print(curr.val,end=" ")
                curr = curr.next
            print()
# deletion at head --> Time complexity O(1) and Space complexity O(1)
    def deleteAtHead(self):
        if self.head is None:
            print("Empty list")
            return
        else:
            self.head = self.head.next 
            if self.head:
                self.head.prev = None
# deletion at tail --> Time complexity O(n) and Space complexity O(1)
    def deleteAtTail(self):
        if self.head is None:
            print("Empty list")
            return
        elif self.head.next is None:
            self.head = None
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.prev.next = None
# deletion at given position --> Time complexity O(n) and Space complexity O(1)
    def deleteAtPosition(self,postion):
        if self.head is None:
            print("Empty list")
            return
        if postion == 0:
            self.deleteAtHead()
            return
        curr = self.head
        count = 0
        while curr and count < postion:
            curr = curr.next 
            count += 1
            