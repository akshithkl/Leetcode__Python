class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        
        # Step 1: Group numbers by digit sum
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            groups[digit_sum] += 1
        
        # Step 2: Find max group size
        max_size = max(groups.values())
        
        # Step 3: Count how many groups have this size
        return sum(1 for size in groups.values() if size == max_size)


# | **Aspect**             | **Details**                                                                                                       |
# | ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
# | **Algorithm**          | Hash Map + Digit Sum Calculation                                                                                  |
# | **Approach/Technique** | Grouping by digit sum, then max + count                                                                           |
# | **Time Complexity**    | **O(n · d)** where `d = digits per number` (≈ O(n log n) in worst case)                                           |
# | **Space Complexity**   | **O(n)** in worst case (if every number has unique digit sum, but practically O(1) since digit sums ≤ 9·log₁₀(n)) |
# | **Key Idea**           | Use hashmap to bucket numbers by digit sum                                                                        |
