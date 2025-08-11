class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


# | Aspect                  | Value                                                                                    |
# | ----------------------- | ---------------------------------------------------------------------------------------- |
# | **Algorithm Approach**  | **Hashing with a Set**                                                                   |
# | **Algorithm Technique** | **Hash Set Lookup** (checks membership in constant average time)                         |
# | **Time Complexity**     | **O(n)** – Each lookup and insert in a set is O(1) on average, repeated for `n` elements |
# | **Space Complexity**    | **O(n)** – In the worst case, all elements are unique, so they all get stored in the set |
# | **Best Case**           | O(1) – If the first two elements are duplicates, early return                            |
# | **Worst Case**          | O(n) – If no duplicates found until the last element                                     |
# | **Why Efficient**       | Uses a hash-based set for O(1) average lookup instead of O(n) search                     |
