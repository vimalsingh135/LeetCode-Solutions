# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)   # placeholder, makes edge cases easy
        tail = dummy           # tail always points to the last node added

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # attach whichever list still has leftover nodes
        tail.next = list1 if list1 else list2

        return dummy.next   # dummy.next is the real head of the merged list
        