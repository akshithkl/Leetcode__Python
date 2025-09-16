# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        # Traverse until they meet or both are None
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA 

# | **Aspect**             | **Details**                                                                                                               |
# | ---------------------- | ------------------------------------------------------------------------------------------------------------------------- |
# | **Algorithm**          | Two-pointer traversal                                                                                                     |
# | **Approach/Technique** | Traverse both lists; when a pointer reaches end, switch to other list’s head until they meet                              |
# | **Time Complexity**    | **O(m + n)** (each pointer traverses both lists once)                                                                     |
# | **Space Complexity**   | **O(1)** (no extra data structures used)                                                                                  |
# | **Key Idea**           | By switching heads, both pointers traverse equal distance (`m + n`), guaranteeing they meet at intersection or at `None`. |
