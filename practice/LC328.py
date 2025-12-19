# we have to place the odd positioned linked list firstly then continued with even linked list 

# brute force soln --> by just changing the value of the linked list , O(n) time and O(n) space
from typing import Optional
class Listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class solution:
    def oddEvenList(self, head):
        temp = head 
        value =  []
        if head or head.next is None :
            return head
        while temp and temp.next:
            value.append(temp)
            temp =  temp.next.next
        temp = head.next
        while temp and temp.next:
            value.append(temp)
            temp =  temp.next.next
        temp = head
        index = 0 
        while temp is not None:
            temp.value =value[index]
            index +=1 
            temp = temp.next
        return head 



#optimal soln :

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next  is None :
            return head 
        even = head.next 
        odd = head 
        even_head = head.next 
        while even is not None and even.next is not None :
            odd.next = odd.next.next 
            odd = odd.next 
            even.next = even.next.next 
            even = even.next 
        odd.next= even_head
        return head 



