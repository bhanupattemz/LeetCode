class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=""
        l1,l2=len(word1),len(word2)
        for i in range(min(l1,l2)):
            result+=(word1[i]+word2[i]) 
        if(l1>l2):
            result+=word1[i+1:]
        elif(l2>l1):
            result+=word2[i+1:]
        return result
    
print(Solution().mergeAlternately("ab","pqrs"))
        