# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        cur = head.next

        while cur:
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
                continue

            temp = dummy
            while cur.val > temp.next.val:
                temp = temp.next
            
            prev.next = cur.next
            cur.next = temp.next
            temp.next = cur
            cur = prev.next
        
        return dummy.next

# | Aspect               | Explanation                                                              |
# | -------------------- | ------------------------------------------------------------------------ |
# | **Algorithm**        | Insertion Sort (adapted for singly linked list)                          |
# | **Approach**         | Iterative, in-place pointer manipulation (dummy node + two pointers)     |
# | **Best Case Time**   | **O(n)** (already sorted list, only one comparison per element)          |
# | **Average Time**     | **O(n²)** (each element may require scanning half of sorted list)        |
# | **Worst Case Time**  | **O(n²)** (reverse sorted list, each insertion scans entire sorted part) |
# | **Space Complexity** | **O(1)** (in-place, uses only pointers and one dummy node)               |
