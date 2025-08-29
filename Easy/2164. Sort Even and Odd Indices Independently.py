class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[0::2])  # non-decreasing
        odd = sorted(nums[1::2], reverse=True)  # non-increasing

        # Merge back
        res = []
        ei, oi = 0, 0  # pointers for even and odd lists

        for i in range(len(nums)):
            if i % 2 == 0:  # even index
                res.append(even[ei])
                ei += 1
            else:           # odd index
                res.append(odd[oi])
                oi += 1

        return res

# | Aspect                  | Details                                                                |
# | ----------------------- | ---------------------------------------------------------------------- |
# | **Algorithm Technique** | Array Partitioning + Sorting + Two-Pointer Merge (Greedy + Sorting)    |
# | **Time Complexity**     | `O(n log n)` (due to sorting both halves)                              |
# | **Space Complexity**    | `O(n)` (extra arrays for even and odd indices + result array)          |
# | **Why Efficient?**      | Sorting dominates; linear steps for splitting and merging are smaller. |
