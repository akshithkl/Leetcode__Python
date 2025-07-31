class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:  # stones are now negative so
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        return abs(stones[0])

# | **Aspect**           | **Details**                                                                                                                                   |
# | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
# | **Approach**         | Greedy + Max-Heap (simulated using min-heap by negating values)                                                                               |
# | **Heap Type**        | Min-heap (used as Max-heap by storing negative values)                                                                                        |
# | **Library Used**     | `heapq` (Python's built-in min-heap implementation)                                                                                           |
# | **Key Operations**   | - Convert values to negatives<br>- `heapify` to build max-heap<br>- `heappop` two heaviest stones<br>- If not equal, push back the difference |
# | **Loop Condition**   | `while len(stones) > 1:` — until 1 or 0 stones remain                                                                                         |
# | **Final Return**     | `abs(stones[0])` if one stone remains; else return `0`                                                                                        |
# | **Time Complexity**  | `O(n log n)`                                                                                                                                  |
# | **Space Complexity** | `O(n)`                                                                                                                                        |
# | **Why Greedy?**      | Always smash the two heaviest stones for optimal reduction                                                                                    |



        
