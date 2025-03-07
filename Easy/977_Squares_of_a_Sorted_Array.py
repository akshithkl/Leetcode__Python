class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in nums:
            val = i * i
            new_nums.append(val)
               
        new_nums.sort() 
       
        return new_nums              #sorted(new_nums) 
        
