class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        
        target = total // 3
        partitions = 0
        running_sum = 0
        
        for num in arr:
            running_sum += num
            if running_sum == target:
                partitions += 1
                running_sum = 0
        
        return partitions >= 3


# | **Aspect**             | **Details**                                              |
# | ---------------------- | -------------------------------------------------------- |
# | **Algorithm**          | Prefix Sum + Greedy Partitioning                         |
# | **Approach/Technique** | One-pass linear scan                                     |
# | **Time Complexity**    | **O(n)** (single traversal of array)                     |
# | **Space Complexity**   | **O(1)** (only counters and sums stored)                 |
# | **Key Idea**           | Cut the array whenever a partition sum reaches `total/3` |
