class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total


# | **Aspect**             | **Details**                               |
# | ---------------------- | ----------------------------------------- |
# | **Algorithm**          | Brute force iteration                     |
# | **Approach/Technique** | Simple loop checking divisibility         |
# | **Time Complexity**    | **O(n)** (checking each number up to `n`) |
# | **Space Complexity**   | **O(1)** (just storing the sum)           |
# | **Key Idea**           | Divisibility check                        |
