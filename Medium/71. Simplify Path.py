class Solution:
    def simplifyPath(self, path: str) -> str:
        stack  = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            
            else:
                cur += c
        
        return "/" + "/".join(stack)

# | Property             | Value                                      |
# | -------------------- | ------------------------------------------ |
# | **Algorithm Type**   | Stack-based simulation                     |
# | **Approach**         | Iterative + Stack                          |
# | **Techniques Used**  | Stack, String Parsing, Simulation          |
# | **Time Complexity**  | `O(n)`                                     |
# | **Space Complexity** | `O(n)` (stack for storing directory names) |
