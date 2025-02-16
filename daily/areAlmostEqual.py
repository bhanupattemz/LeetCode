class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if(s1==s2):
            return True
        l1=list(s1)
        l2=list(s2)
        for i in range(len(s2)):
            for j in range(i+1,len(s2)):
                l2[i],l2[j]=l2[j],l2[i]
                if(l2==l1):
                    return True
                l2[i],l2[j]=l2[j],l2[i]
        return False

print(Solution().areAlmostEqual("bank","kanb"))