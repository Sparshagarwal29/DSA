class ListNode_o:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class soln_o:
    def middleNode_o(self,head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow



            
