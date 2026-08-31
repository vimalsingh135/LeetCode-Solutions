# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes left starting from `head`
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head  # fewer than k nodes left, leave as is

        # Reverse the first k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # `curr` now points to the (k+1)-th node — recurse on the rest
        # `head` is now the tail of this reversed group; connect it to the
        # result of reversing the remaining list
        head.next = self.reverseKGroup(curr, k)

        return prev  # prev is the new head of this reversed group