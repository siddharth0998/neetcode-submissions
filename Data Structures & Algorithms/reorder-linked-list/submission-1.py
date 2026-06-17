# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1,l2 = head,slow.next
        slow.next = None

        prev,start = None,l2

        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp

        revl2 = prev

        while l1 and revl2:
            nextl1 = l1.next
            nextl2 = revl2.next

            l1.next = revl2
            revl2.next = nextl1

            l1 = nextl1
            revl2 = nextl2






