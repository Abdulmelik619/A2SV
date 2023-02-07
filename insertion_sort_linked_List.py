# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node_list = []
        while head:
            node_list.append(ListNode(head.val))
            head = head.next
        
        def output_val(node):
            return node.val
        node_list.sort(key = output_val)
        
        for i, item in enumerate(node_list):
            item.next = node_list[i+1] if i<len(node_list)-1 else None
        return node_list[0]
