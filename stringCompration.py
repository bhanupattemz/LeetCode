class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result=[]
        index=-1
        l=1
        for i in range(len(chars)):
            if index==-1:
                result.append(chars[i])
                index=i
            elif chars[index]==chars[i]:
                l+=1
                if(len(chars)==i+1):
                    for num in str(l):
                        result.append(num)
            else:
                if l>1:
                    for num in str(l):
                        result.append(num)
                    l=1
                result.append(chars[i])
                index=i
        for i in range(len(result)):
            chars[i]=result[i]
        [chars.pop() for j in range(i+1,len(chars))] 
        return result
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))