# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer and fast_pointer:
            if slow_pointer == fast_pointer:
                return True
            if slow_pointer.next == None:
                break 
            if fast_pointer.next == None or fast_pointer.next.next == None:
                break 
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return False