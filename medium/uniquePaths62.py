class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        def find(i, j):
            if i == m - 1 and j == n - 1:  
                return 1
            if i >= m or j >= n:  
                return 0
            if dp[i][j] != -1:  
                return dp[i][j]
            
            dp[i][j] = find(i + 1, j) + find(i, j + 1) 
            return dp[i][j]

        return find(0, 0)

print(Solution().uniquePaths(3, 7))  
