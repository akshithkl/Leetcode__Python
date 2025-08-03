class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False

# | Metric    | Complexity                                       |
# | --------- | ------------------------------------------------ |
# | **Time**  | O(n × target) in the worst case                  |
# | **Space** | O(target) — due to set size being up to `target` |

# | --------------- | ------------------------------------------------- |
# | **Approach**    | DP with sets for subset-sum tracking              |
# | **Algorithm**   | Bottom-Up Dynamic Programming                     |
# | **When useful** | When exact subset-sum needed (e.g., Leetcode 416) |
# | **Early exit**  | If we find a sum == `target`, return early        |
