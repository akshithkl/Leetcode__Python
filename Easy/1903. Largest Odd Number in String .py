class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:  # check if odd
                return num[:i+1]
        return "" 
        

# | Aspect                  | Details                     |
# | ----------------------- | --------------------------- |
# | **Algorithm Technique** | Greedy + Right-to-Left Scan |
# | **Time Complexity**     | O(n)                        |
# | **Space Complexity**    | O(n) (substring storage)    |


        
