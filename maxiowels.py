class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels=["a","e","i","o","u"]
        maxi=0
        subString=s[0:k]
        for j in subString:
                if j in vowels:
                    maxi+=1
        numvowels=maxi
        for i in range(1,len(s)-k+1):
            if subString[0] in vowels:
                numvowels-=1
            if s[i+k-1] in vowels:
                numvowels+=1
            subString=s[i:i+k]
            if maxi<numvowels:
                maxi=numvowels
        return maxi
print(Solution().maxVowels("abciiidef",3))