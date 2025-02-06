class Solution:
    def climbStairs(self, n: int) -> int:
        
        memory = [0] * (n+1)

        def climb(i, n, memory):
            if i > n:
                return 0
            if i == n:
                return 1
            if memory[i] > 0:
                return memory[i]
            
            memory[i] = climb(i+1, n, memory) + climb(i+2, n, memory)
            return memory[i]
        return climb(0, n, memory)
