class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res

# | Aspect                  | Details                                                                                                                                                                                                                                              |
# | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | **Algorithm Technique** | Backtracking + Sorting + Handling duplicates (skip duplicates using while loop)                                                                                                                                                                      |
# | **Time Complexity**     | $O(2^n \cdot n)$ in worst case, where $n$ is the number of elements in `nums`. <br>Explanation: There are up to $2^n$ subsets. Copying each subset takes $O(n)$ time. Sorting takes $O(n \log n)$. Overall worst-case dominated by $O(2^n \cdot n)$. |
# | **Space Complexity**    | $O(n)$ recursion stack + $O(2^n \cdot n)$ for storing all subsets in `res`                                                                                                                                                                           |
# | **Key Idea / Approach** | - Sort the array to group duplicates together. <br>- Use backtracking to generate all subsets. <br>- Skip over duplicate elements after exploring including one occurrence to avoid duplicate subsets.                                               |
