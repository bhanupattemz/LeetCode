class Solution:
    def longestMonotonicSubarray(self, nums) -> int:
        increase=1
        decrease=1
        m=0
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                increase+=1
                m=max(m,decrease)
                decrease=1
            elif nums[i]<nums[i-1]:
                decrease+=1
                m=max(m,increase)
                increase=1
            else:
                m=max(increase,decrease,m)
                increase=1
                decrease=1

        return max(increase,decrease,m)

print(Solution().longestMonotonicSubarray([3,3,3,3]))