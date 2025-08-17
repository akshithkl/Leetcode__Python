class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            # check if current and next are bad pair
            if (s[i].lower() == s[i+1].lower()) and (s[i] != s[i+1]):
                # remove them
                s = s[:i] + s[i+2:]
                # go one step back if possible (to recheck new neighbors)
                if i > 0:
                    i -= 1
            else:
                i += 1
        return s

# | Aspect             | Details                          |
# | ------------------ | -------------------------------- |
# | Algorithm Approach | Greedy / Iterative / Two-pointer |
# | Technique          | Scan + Remove + Backtrack        |
# | Time Complexity    | O(n²) worst-case, O(n) best-case |
# | Space Complexity   | O(1) extra                       |
