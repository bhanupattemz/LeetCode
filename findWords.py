class Solution:
    def findWords(self, board, words):
        result = set()
        rows, cols = len(board), len(board[0])
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["#"] = word  
        
        def dfs(r, c, node, visited):
            char = board[r][c]
            if char not in node:
                return
            node = node[char]
            if "#" in node:
                result.add(node["#"])  
            
            visited.add((r, c)) 
        
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(nr, nc, node, visited)
            
            visited.remove((r, c))  
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie, set())
        
        return list(result)


# Example usage:
board = [["a","b","c","e"], ["x","x","c","d"], ["x","x","b","a"]]
words = ["abc", "abcd"]
print(Solution().findWords(board, words))
