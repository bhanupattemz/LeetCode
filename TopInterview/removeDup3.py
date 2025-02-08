class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return nums
print(Solution().removeDuplicates([1,2,3,2,3,1,34,6]))