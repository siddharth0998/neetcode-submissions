# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.kthNode(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = groupNext, groupPrev.next
            tmp_grupCurr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            groupPrev.next = kth
            groupPrev = tmp_grupCurr
        return dummy.next


    def kthNode(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr