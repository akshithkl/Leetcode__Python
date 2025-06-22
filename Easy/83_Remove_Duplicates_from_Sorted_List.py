# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate
            else:
                current = current.next  # Move to next node
        
        return head


# Time Complexity: O(n) — We traverse the list once.

# Space Complexity: O(1) — In-place removal, no extra memory used.

# | Category           | Description                                          |
# | ------------------ | ---------------------------------------------------- |
# | **Algorithm**      | Iterative Linked List Traversal                      |
# | **Approach**       | Single Pass (Linear Scan)                            |
# | **Technique**      | **Two-pointer technique** (current and current.next) |
# | **Data Structure** | Singly Linked List                                   |
# | **Optimization**   | In-place removal of duplicates (`O(1)` extra space)  |
