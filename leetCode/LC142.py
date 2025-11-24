# we have to just check if their id cycle present in the linked list of not 


# brute force soln , Time and space is O(N)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        temp = head
        visited = set()

        while temp:
            if temp in visited:
                return temp
            visited.add(temp)
            temp = temp.next
        
        return None



#  optimal time is O(N) btte space is O(1)
class ListNodeOPP:
    def __init__(self, x):
        self.val = x
        self.next = None
class SolutionOPP:
    def detectCycle(self, head):
        slow = head
        fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None