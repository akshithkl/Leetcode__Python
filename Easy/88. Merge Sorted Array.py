class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead."""

        #  last index nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n -1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
            
        # fill the nums1 leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1 


# | **Time Complexity**  | `O(m + n)` | Each element from `nums1` and `nums2` is visited once during the merge. |
# | **Space Complexity** | `O(1)`     | In-place merge. No extra data structures used (constant extra space).   |

# | **Algorithm**          | Merge Sorted Arrays                                                   |
# | **Technique**          | **Two-Pointer Technique** (in reverse direction)                      |
# | **Why Reverse Merge?** | Avoids overwriting `nums1`'s valid elements by starting from the back |
# | **In-Place**           | Yes – modifies `nums1` without using additional space                 |
# | **Stable Sort?**       | No – not guaranteed; but not required in this problem                 |
