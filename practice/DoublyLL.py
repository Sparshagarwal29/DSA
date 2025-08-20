class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class doublyLinkedList:
    def __init__(self):
        self.head = None
#           INSERTION
    def InsertAtBeggining(self,val):
        new_node = Node(val)
        if self.head is  None:
            self.head = new_node
        else:
            new_node.next = self.head # type: ignore
            self.head.prev = new_node # type: ignore
            self.head = new_node
        
    def InsertAtEnd(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node # type: ignore
            new_node.prev = curr # type: ignore
        
    def InsertAtPosition(self,val,postion):
        new_node = Node(val)
        if postion == 0:
            self.InsertAtBeggining(val)
            return
        else:
            curr = self.head
            count = 0 
            while curr and count < postion -1:
                curr = curr.next
                count +=1
            if curr is None:
                print("postion out of bound")
                return
            new_node.next =  curr.next 
            new_node.prev = curr # type: ignore
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node # type: ignore
        
