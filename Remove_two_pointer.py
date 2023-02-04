# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            if head.next is not None:
                if head.val == head.next.val:
                    headTemp = self.deleteDuplicates(head.next)
                    if headTemp is not None:
                        if head.val == headTemp.val:
                            if headTemp is not None:
                                return headTemp.next
                            return None
                    return headTemp
                else:
                    head.next = self.deleteDuplicates(head.next)
        return head
