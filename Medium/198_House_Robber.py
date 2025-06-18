class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


# Time Complexity: O(N)
# Space Complexity: O(1)
"""
| Attribute      | Description                                        |
| -------------- | -------------------------------------------------- |
| **Algorithm**  | **Dynamic Programming**                            |
| **Approach**   | **Bottom-Up (Tabulation)**                         |
| **Technique**  | **Space-Optimized DP** using two variables         |
| **Pattern**    | **Maximum Non-Adjacent Sum**                       |
| **Time**       | `O(n)`                                             |
| **Space**      | `O(1)`                                             |
| **Strengths**  | Fast, clean, optimal space                         |
| **Weaknesses** | No recursion insight; harder to trace step-by-step |
"""
