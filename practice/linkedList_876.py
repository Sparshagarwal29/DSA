# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# BRUTE FORCE SOLN :
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class soln:
    def middleNode(self,head):
        temp = head
        n = 0 
        while temp is not None:
            n +=1
            temp = temp.next
        temp = head
        for i in range(n//2):
            temp = temp.next
        return temp
    
# Optimal soln (totoniesr hair approch )
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



            
