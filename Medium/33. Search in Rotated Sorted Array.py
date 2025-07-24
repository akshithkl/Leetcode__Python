class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion 
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # right  sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return  - 1

            
# | **Category**         | **Details**                                                                                             |
# | -------------------- | ------------------------------------------------------------------------------------------------------- |
# | **Problem**          | Search an element in a **rotated sorted array**                                                         |
# | **Algorithm**        | **Modified Binary Search**                                                                              |
# | **Approach**         | **Divide and Conquer**                                                                                  |
# | **Technique**        | - Binary Search<br>- Two Pointers (`l`, `r`)<br>- Sorted portion check<br>- Condition-based elimination |
# | **Time Complexity**  | `O(log n)`                                                                                              |
# | **Space Complexity** | `O(1)`                                                                                                  |
# | **Why O(log n)?**    | Search space is halved in each iteration                                                                |
# | **Why O(1) space?**  | No extra memory or recursion stack used                                                                 |
# | **Used For**         | Arrays that are **rotated but sorted**                                                                  |
# | **Key Logic**        | Always one side (left or right) is sorted — use that to discard half search space                       |
