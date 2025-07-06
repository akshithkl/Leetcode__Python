class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the characters
            s[left], s[right] = s[right], s[left]
            # Move pointers
            left += 1
            right -= 1
      


# | Aspect        | Description                   |
# | ------------- | ----------------------------- |
# | **Algorithm** | Two-Pointer                   |
# | **Approach**  | In-Place Swapping             |
# | **Technique** | Two-Pointer, In-Place, Greedy |
# | **Time**      | O(n)                          |
# | **Space**     | O(1) (no extra memory used)   |
