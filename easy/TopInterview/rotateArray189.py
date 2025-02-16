class Solution:
    def rotate(self, nums, k: int):
        l=len(nums)
        k=k%l
        nums[0:]=nums[l-k:]+nums[:l-k]
        