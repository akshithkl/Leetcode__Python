class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # try all possible first and second numbers
        for i in range(1, n):
            if num[0] == "0" and i > 1:   # leading zero in first number
                break
            a = int(num[:i])
            
            for j in range(i + 1, n):
                if num[i] == "0" and j - i > 1:   # leading zero in second number
                    break
                b = int(num[i:j])
                
                if self.check(num, j, a, b):
                    return True
        return False
    
    def check(self, s: str, start: int, a: int, b: int) -> bool:
        n = len(s)
        made_third = False   # must ensure at least 3 numbers
        
        while start < n:
            c = a + b
            c_str = str(c)
            if not s.startswith(c_str, start):
                return False
            start += len(c_str)
            a, b = b, c
            made_third = True
        return made_third

# | Metric             | Value                                |
# | ------------------ | ------------------------------------ |
# | Algorithm Approach | Brute-force search + Simulation      |
# | Technique          | String parsing + Iterative sum check |
# | Time Complexity    | O(n³)                                |
# | Space Complexity   | O(1)                                 |
