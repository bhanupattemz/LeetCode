class Solution:
    def isArraySpecial(self, nums) -> bool:
        if(len(nums)==1):
            return True

        result=nums[0]%2==0
        for i in range(1,len(nums)):
            temp=nums[i]%2==0
            if(temp and result) or (not temp and not result):
                return False
            result=temp
        return True
            

        