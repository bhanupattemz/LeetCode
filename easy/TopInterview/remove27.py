class Solution:
    def removeElement(self, nums, val: int):
        while val in nums:
            nums.pop(nums.index(val))
        return nums
print(Solution().removeElement([1,22,3,4,3,4,3],3))