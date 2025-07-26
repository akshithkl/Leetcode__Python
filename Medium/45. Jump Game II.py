class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0 

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        
        return res

# | **Aspect**            | **Value**                                                                |
# | --------------------- | ------------------------------------------------------------------------ |
# | **Algorithm**         | Greedy                                                                   |
# | **Approach**          | Sliding Window using Greedy                                              |
# | **Technique**         | Level-by-level BFS-like traversal (but optimized using greedy)           |
# | **Time Complexity**   | `O(n)`                                                                   |
# | **Space Complexity**  | `O(1)` (no extra data structures used)                                   |
# | **Optimized?**        | Yes – optimal greedy solution (better than DP approach for large inputs) |
# | **Problem Type**      | Greedy, Array Traversal                                                  |
# | **Input Constraints** | `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 1000`                       |
