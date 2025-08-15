# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# | Aspect                  | Details                                                                                                                  |
# | ----------------------- | ------------------------------------------------------------------------------------------------------------------------ |
# | **Algorithm technique** | **Two-pointer (Tortoise and Hare)**                                                                                      |
# | **Time Complexity**     | **O(N)** → Each pointer traverses at most `N` nodes, so the total is linear.                                             |
# | **Space Complexity**    | **O(1)** → No extra space used apart from a few pointers.                                                                |
# | **Reasoning**           | The `fast` pointer moves twice as fast as `slow`. When `fast` reaches the end, `slow` will be at the middle of the list. |
