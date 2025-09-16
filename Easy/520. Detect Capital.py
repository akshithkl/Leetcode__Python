
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All uppercase
        if word.isupper():
            return True
        # Case 2: All lowercase
        if word.islower():
            return True
        # Case 3: First letter uppercase and rest lowercase
        if word[0].isupper() and word[1:].islower():
            return True
        return False


# | **Aspect**             | **Details**                                         |
# | ---------------------- | --------------------------------------------------- |
# | **Algorithm**          | String checking using built-in methods              |
# | **Approach/Technique** | Case analysis with `isupper()`, `islower()`         |
# | **Time Complexity**    | **O(n)** (string scanning by Python built-ins)      |
# | **Space Complexity**   | **O(1)** (no extra data structures)                 |
# | **Key Idea**           | Use Python’s built-in string methods for simplicity |
