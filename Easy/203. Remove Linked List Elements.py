# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        curr = head

        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            
            curr = nxt
        return dummy.next

#  Two pointer Tecnique
# Time complexity : O(n)
#  Space complexity : O(1)
