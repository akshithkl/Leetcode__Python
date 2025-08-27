class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        
        for n in nums:
            if n in (first, second, third):  # skip duplicates
                continue
            
            if n > first:
                first, second, third = n, first, second
            elif n > second:
                second, third = n, second
            elif n > third:
                third = n
        
        return third if third != float('-inf') else first


# | Aspect                  | Details                                         |
# | ----------------------- | ----------------------------------------------- |
# | **Algorithm Technique** | Single-pass selection (tracking top-3 maximums) |
# | **Time Complexity**     | O(n)                                            |
# | **Space Complexity**    | O(1)                                            |
# | **Why Efficient?**      | No sorting (O(n log n)), no extra memory        |

  
