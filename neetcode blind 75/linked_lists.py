class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head 

        while curr:
            curr_next = curr.next 
            curr.next = prev
            prev = curr 
            curr = curr_next
        return prev 
    

n1 = ListNode(30)
n2 = ListNode(20, n1)
n3 = ListNode(10, n2)
sol = Solution().reverseList(n3)
print(sol.val, sol.next.val)