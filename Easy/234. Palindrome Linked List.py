# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next 
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True 

# | Aspect    | Value                      |
# | --------- | -------------------------- |
# | **Time**  | `O(n)`                     |
# | **Space** | `O(1)` (in-place reversal) |

# Two Pointer Technique (Fast & Slow)

# In-place Reversal of Linked List

# Pointer Comparison
