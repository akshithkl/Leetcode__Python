class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for start in range(0, len(chars), 2 * k):
            left = start
            right = min(start + k - 1, len(chars) - 1)

            while left < right:
                chars[left],chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)

# | **Aspect**               | **Details**                                                                                                             |
# | ------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
# | **Problem Type**         | String manipulation                                                                                                     |
# | **Algorithm Technique**  | **Two-Pointer Approach** + **Greedy Iterative Processing**                                                              |
# | **Approach**             | Process the string in chunks of size `2k`, reversing the first `k` characters of each chunk using two-pointer swapping. |
# | **Time Complexity**      | **O(n)** — Outer loop runs \~`n/(2k)` times, inner loop swaps ≤ `k/2` pairs each time → overall proportional to `n`.    |
# | **Space Complexity**     | **O(n)** — Due to conversion of string to list for mutability (if input was mutable, would be O(1)).                    |
# | **Best Case**            | **O(n)** — Still must scan through all characters.                                                                      |
# | **Worst Case**           | **O(n)** — Each character is processed at most once.                                                                    |
# | **Extra Space Used**     | List copy of string (n elements) + a few integers (O(1)).                                                               |
# | **In-place?**            | No (because of immutable string in Python), but swapping happens in the list version.                                   |
# | **Category**             | String Manipulation, Two-Pointer, Iterative Greedy                                                                      |
# | **Stability**            | Not applicable (not a sorting problem)                                                                                  |
# | **Data Structures Used** | List (for mutable string operations)                                                                                    |

        
