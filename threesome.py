class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result=[]
        def sumcheck(data):
            length=len(data) 
            for i in range(length):
                num2= sumcheck(data[i+1:])
                num3=sumcheck(data[i+2:])
                if num2!=None and num3!=None:
                    sums=sum([data[i],num2,num3])
                    print(data[i])
                    if sums==0:
                        result.append([data[i],num2,num3])
                return data[i] 
        sumcheck(nums)
        # for i in range(length):
        #     sums[0]=nums[i]
        #     for j in range(i+1,length-1):
        #         sums[1]=nums[j]
        #         sums[2]=nums[j+1]
        #         if sum(sums)==0:
        #             result.append(sums[0:])
        return result

print(Solution().threeSum([-1,0,1,2,-1,-4]))