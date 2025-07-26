class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        for i in range(n - m + 1):  # Loop until there's space for needle
            if haystack[i:i+m] == needle:
                return i
        return -1

        


# | Aspect        | Description                         |
# | ------------- | ----------------------------------- |
# | **Algorithm** | Naive String Matching               |
# | **Technique** | Sliding Window + String Comparison  |
# | **Approach**  | Brute Force Substring Comparison    |

#  Time Complexity 
# | Best  | O(m)                          |
# | Worst | O((n - m + 1) × m) ≈ O(n × m) |

# Space Complexity | O(1)  |
