class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b
# | Item                 | Value                                  |
# | -------------------- | -------------------------------------- |
# | **Algorithm**        | Dynamic Programming                    |
# | **Approach**         | Bottom-Up Tabulation                   |
# | **Technique**        | State Transition, Optimal Substructure |
# | **Time Complexity**  | O(n)                                   |
# | **Space Complexity** | O(1) (optimized)               |
