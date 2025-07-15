# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
 
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1
            first, second = temp1, temp2


# | **Aspect**           | **Value**                                                           |
# | -------------------- | ------------------------------------------------------------------- |
# | **Algorithm**        | Linked List Manipulation                                            |
# | **Approach**         | Two Pointers + Reverse Second Half + Merge Alternately              |
# | **Technique**        | Fast and Slow Pointer, In-place Reversal, Pointer Rewiring          |
# | **Time Complexity**  | O(n) — Traverse list to find middle, reverse second half, and merge |
# | **Space Complexity** | O(1) — In-place manipulation, no extra memory used                  |
# | **Best Case**        | O(n) — Always needs full traversal regardless of list layout        |
# | **Worst Case**       | O(n) — Worst case is same as best (linear in all steps)             |
# | **Stable?**          | Not stable (reorders node positions)                                |
# | **In-Place?**        | Yes                                                                 |
# | **Input**            | Head of singly linked list                                          |
# | **Output**           | Modified list with reordered nodes in-place                         |
# | **Example Input**    | 1 → 2 → 3 → 4 → 5                                                   |
# | **Example Output**   | 1 → 5 → 2 → 4 → 3                                                   |
# | **Used For**         | Reordering nodes for problems like LeetCode 143 — Reorder List      |
