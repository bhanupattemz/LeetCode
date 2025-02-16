class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                result[i][j]=matrix[len(matrix)-1-j][i]
        return result
print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))