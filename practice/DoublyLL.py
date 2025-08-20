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

    def DeleteAtbegining(self):
        if self.head is None:
            print("empty List")
        elif self.head.next is None:
            self.head = None
            return
        else:
            self.head.next.prev = None 
            self.head = self.head.next
    def DeleteAtEnd(self):
        if self.head == None:
            print("empty")
        elif self.head.next == None:
            self.head = None
            return
        else:
            temp = self.head
            while temp.next.next is not None: # type: ignore
                temp = temp.next # type: ignore
            temp.next.prev = None # type: ignore
            temp.next = None   # type: ignore
    def deleteSpecificVal(self,val):
        if self.head is None:
            print("empty")
        if self.head.val == val:   # type: ignore
            if self.head.next is None:   # type: ignore
                self.head = None
            else:  
                self.head.next.prev = None  # type: ignore
                self.head = self.head.next  # type: ignore
            return
        temp = self.head.next  # type: ignore
        while temp is not None:
            if temp.val == val:
                temp.prev.next = temp.next 
                if temp.next is not None:
                    temp.next.prev = temp.prev
                return
            temp = temp.next 
    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()
    def traverse_backword(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.val) 
            curr = curr.prev
        print()
                

