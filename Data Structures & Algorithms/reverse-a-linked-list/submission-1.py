# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        left = head
        if left.next is not None:
            right = left.next
            left.next = None
        else:
            return left

        while right.next is not None:
            temp_next = right.next
            right.next = left
            left = right
            right = temp_next
        right.next = left
        return right
