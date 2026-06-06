# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        l = dummy
        r = head

        cnt = 0
        while cnt < n:
            r = r.next
            cnt += 1

        while r:
            l = l.next
            r = r.next

        temp = l.next.next
        l.next = temp
        return dummy.next




