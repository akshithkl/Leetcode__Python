class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            y = target - nums[x]
            if y in hashmap :
                return hashmap[y],x
            else:
                hashmap[nums[x]] = x
     
