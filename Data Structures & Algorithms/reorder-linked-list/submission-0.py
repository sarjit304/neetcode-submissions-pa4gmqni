# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head:
            curr = head
            while curr is not None and curr.next is not None and curr.next.next is not None:
                secondLastElement = self.getLastElementAddress(curr)
                self.appendNext(curr, secondLastElement.next)
                secondLastElement.next = None
                curr = curr.next.next
        
        return None

    def getLastElementAddress(self, currentNode):
        if currentNode.next is None or currentNode.next.next is None:
            return None
        while currentNode.next.next:
            currentNode = currentNode.next
        return currentNode


    def appendNext(self, currentNode, newNode):
        temp = currentNode.next
        currentNode.next = newNode
        newNode.next = temp