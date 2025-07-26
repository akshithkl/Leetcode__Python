class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 0, x
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                result = mid  # store best so far
                left = mid + 1
            else:
                right = mid - 1
        
        return result


# | Aspect               | Value                   |
# | -------------------- | ----------------------- |
# | **Algorithm**        | Binary Search           |
# | **Time Complexity**  | `O(log x)`              |
# | **Space Complexity** | `O(1)`                  |
# | **Technique**        | Binary Search on Answer |
