class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not(str1 or str2):
            return ""
        l1,l2=len(str1),len(str2)
        result=""
        for letter in range(l1):
            i,j=letter,0
            letters=""
            while i<l1 and j<l2:
                if(str1[i]==str2[j]):
                    letters+=str1[i]
                    i+=1
                    j+=1
                elif (not str1[i]==str2[j]) and len(letters)>0:
                    if(len(result)<len(letters)): result=letters
                    letters=""
                    i=letter
                else:
                    j+=1
            if(len(result)<len(letters)): result=letters
        return result
print(f'answer:{Solution().gcdOfStrings("","")}')
                