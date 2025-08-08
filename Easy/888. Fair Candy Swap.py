class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumB - sumA) // 2
        
        # Convert bobSizes to set for O(1) lookup
        bobSet = set(bobSizes)
        
        for x in aliceSizes:
            y = x + diff
            if y in bobSet:
                return [x, y]


# | Item                 | Value                                |
# | -------------------- | ------------------------------------ |
# | **Algorithm Type**   | Hashing + Math (Greedy-style logic)  |
# | **Approach**         | Use math to reduce problem to lookup |
# | **Time Complexity**  | O(n + m)                             |
# | **Space Complexity** | O(m)                                 |
