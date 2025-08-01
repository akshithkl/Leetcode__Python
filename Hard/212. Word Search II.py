class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if ( r < 0 or c < 0 or r == rows or c == cols or
             board[r][c] not in node.children or (r, c) in visit):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)

# | Aspect           | Value                                                            |
# | ---------------- | ---------------------------------------------------------------- |
# | Algorithm        | Trie + DFS with Backtracking                                     |
# | Time Complexity  | O(M × N × 4^L)  <br> where L = max word length, M×N = board size |
# | Space Complexity | O(K × L) for Trie <br> + O(L) DFS call stack                     |
# | Optimizations    | Using Trie avoids checking invalid prefixes early                |
# | Problem Type     | Backtracking + Trie                                              |
