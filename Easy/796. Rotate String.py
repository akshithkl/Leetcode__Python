class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

       # Try all possible rotations
        for i in range(len(s)):
        # Rotate s by i positions
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True

        return False

# | Metric               | Value                      |
# | -------------------- | -------------------------- |
# | **Algorithm**        | Brute-force rotation check |
# | **Time Complexity**  | O(n²)                      |
# | **Space Complexity** | O(n)                       |
# | **Optimized?**       | No (brute force)           |
