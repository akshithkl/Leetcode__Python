
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])  # Fix tuple append

                    while l < r and nums[l] == nums[l + 1]:  # Skip duplicates for l
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:  # Skip duplicates for r
                        r -= 1

                    l += 1
                    r -= 1

        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])  # Fix tuple append

                    while l < r and nums[l] == nums[l + 1]:  # Skip duplicates for l
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:  # Skip duplicates for r
                        r -= 1

                    l += 1
                    r -= 1

        return res
