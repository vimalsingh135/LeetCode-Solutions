# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # move fast n+1 steps ahead so there's a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # slow is now right before the node to delete
        slow.next = slow.next.next

        return dummy.next