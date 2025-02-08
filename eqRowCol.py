class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        result=0
        for i in range(n):
            list=[]
            for j in range(n):
                list.append(grid[j][i])
            for j in range(n):
                if list==grid[j]:
                    result+=1
        return result
        
print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))