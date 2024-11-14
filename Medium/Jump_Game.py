class Solution:
    def canJump(self, nums: List[int]) -> bool:
        parent_right = 0

        for i, x in enumerate(nums):

            if i > parent_right:
                return False
            
            parent_right = max(parent_right, i + x)
        return True
