class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        data={'(':')','[':']','{':'}'}
        list=[]
        l=0
        for item in s:
            if item in data:
                list.append(item)
                l+=1
            elif len(list)!=0 and item==data[list[len(list)-1]]:
                list.pop()
            else:
                return False
        if 2*l!=len(s):
            return False
        return True
print(Solution().isValid("({})"))