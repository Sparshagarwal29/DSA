#  we have to find the length of the cycle of the linked list not the whole linked list just from the point the cycle start 

# brute force both O(n)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        temp = head
        my_dic = dict()
        travel = 0 
        while temp is not None:
            if temp in my_dic:
                return travel - my_dic[temp]
            my_dic[temp]= travel
            travel +=1 
            temp = temp.next
        return 0 
    

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
                slow = slow.next 
                count = 1 
                while slow != fast:
                    slow = slow.next 
                    count +=1 

        return None
    