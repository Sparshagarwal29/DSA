# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []




# this is brute force soln , we will first calculate the length of linked list then we will traverse again to the (length - n)th node and then we will change its next pointer to next of next pointer
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = 0 
        temp = head 
        while temp is not None:
            length +=1 
            temp = temp.next 
        if length == n:
            return head.next 
        temp = head 
        for i in range(length - n - 1):
            temp = temp.next 
        temp.next = temp.next.next 
        return head  


