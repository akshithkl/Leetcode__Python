class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            num = sum_digits
        return num

# | **Aspect**           | **Value**                                                        |
# | -------------------- | ---------------------------------------------------------------- |
# | **Time Complexity**  | `O(log n)` per digit-summing iteration, total `O(log n)` overall |
# | **Space Complexity** | `O(1)` — uses only constant extra space                          |
# | **Algorithm**        | Brute-force, repeated digit summation                            |
# | **Technique**        | Looping, Math (Digit Processing)                                 |
