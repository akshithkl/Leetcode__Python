class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if num >= 100 and num % 2 == 0:
                            res.add(num)

        return sorted(res)

# | **Aspect**             | **Details**                                                                 |
# | ---------------------- | --------------------------------------------------------------------------- |
# | **Algorithm**          | Brute-force triple nested loop                                              |
# | **Approach/Technique** | Generate all permutations of 3 digits & filter                              |
# | **Time Complexity**    | **O(n³ · log m)** → because of triple loop + sorting (`m` = size of result) |
# | **Space Complexity**   | **O(m)** for storing valid numbers in a set                                 |
# | **Key Idea**           | Enumerate every possible 3-digit number and filter                          |
