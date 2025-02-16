class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        data={'2':'abc',
              '3':'def',
              '4':'ghi',
              '5':'jkl',
              '6':'mno',
              '7':'pqrs',
              '8':'tuv',
              '9':'wxyz'}
        result=[]
        def com(combination,next_digits):
            if not next_digits:
                result.append(combination)      
                return
            for letter in data[next_digits[0]]:
                com(combination+letter,next_digits[1:])
        com("",digits)
            
        return result

print(Solution().letterCombinations("23"))