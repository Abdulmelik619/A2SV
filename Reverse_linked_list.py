# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        AList=[]
        a=head
        while(head):
            AList.append(head.val)
            head=head.next
        ans=ListNode(0) 
        tmp=ans
        AList.reverse()
        for x in AList:
            tmp.next = ListNode(x)
            tmp =  tmp.next
        return ans.next
        


