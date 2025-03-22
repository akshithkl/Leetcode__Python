class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0 
        L, R = 0, len(height) - 1

        while L < R:
            area = (R - L) * min(height[L], height[R])
            res = max(res, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return res
        
