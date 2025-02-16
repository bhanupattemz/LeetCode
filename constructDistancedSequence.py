class Solution:
    def constructDistancedSequence(self, n: int):
        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        self.backtrack(result, used, n, 0)
        return result

    def backtrack(self, result, used, n: int, index: int):
        while index < len(result) and result[index] != 0:
            index += 1
        if index == len(result):
            return True
        for i in range(n, 0, -1):
            if used[i]:
                continue
            if i == 1:
                result[index] = 1
                used[1] = True
                if self.backtrack(result, used, n, index + 1):
                    return True
                result[index] = 0
                used[1] = False
            elif index + i < len(result) and result[index + i] == 0:
                result[index] = i
                result[index + i] = i
                used[i] = True
                if self.backtrack(result, used, n, index + 1):
                    return True
                result[index] = 0
                result[index + i] = 0
                used[i] = False
        return False
            
                

print(Solution().constructDistancedSequence(5))