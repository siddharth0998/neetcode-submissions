# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def merge(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        curr.next = list1 or list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        l,r = 0, n-1
        mid = (r - l) // 2 + l
        left = self.mergeKLists(lists[l:mid+1])
        right = self.mergeKLists(lists[mid+1:n])
        return self.merge(left,right)