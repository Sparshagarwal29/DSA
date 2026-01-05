# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []




# this is brute force soln , we will first calculate the length of linked list then we will traverse again to the (length - n)th node and then we will change its next pointer to next of next pointer
# time complexity O(n){its more importantly in 2n} and space complexity O(1), it is also writen we need to do in single pass 
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


# this is the optimal soln where we will use two pointer approach , we will move fast pointer n steps ahead and then we will move both slow and fast pointer until fast pointer reaches the end of linked list , at that point slow pointer will be at (length - n)th node
class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class solution:
    def removeNthFromEnd(self, head, n: int):
        slow = head 
        fast = head 
        for _ in range(n):
            fast = fast.next 
        if fast == None :
            return head.next 
        while fast.next is not None :
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next
        return head 