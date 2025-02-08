class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alph="abcdefghijklmnopqrstuvwxyz"
        index=[]
        for item in alph:
            ind=s.find(item)
            if ind!=-1 and item not in s[ind+1:]:
                index.append(ind)            
        return min(index) if index else -1
print(Solution().firstUniqChar("aa"))