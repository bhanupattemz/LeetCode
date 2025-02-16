class Solution:
    def maxAscendingSum(self, nums) -> int:
        m = 0
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                sum += nums[i]
            else:
                m = max(sum, m)
                sum = nums[i]
        return max(sum, m)

print(Solution().maxAscendingSum([10,20,30,5,10,50]))