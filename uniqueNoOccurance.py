class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        result=[]
        while len(arr)!=0:
            i=arr[0]
            n=1
            arr.remove(i)
            while True:
                if i in arr:
                    n+=1
                    arr.remove(i)
                else:
                    break
            if n in result:
                return False
            result.append(n)
        return True
print(Solution().uniqueOccurrences([1,2]))