class Solution:
    def check(self, nums) -> bool:
        sorted=[i for i in nums]
        sorted.sort()
        l=len(nums)
        rotated=[0]*l+[i for i in nums]
        start=l-1
        end=2*l-1
        while start>=0:
            rotated[start]=rotated[end]
            if(rotated[start:end]==sorted):
                return True
            start-=1
            end-=1
        return False
print(Solution().check([2,1,3,4]))