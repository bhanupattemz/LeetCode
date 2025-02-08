class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        while True:
            if 0 in nums[0:len(nums)-i]:
                nums.remove(0)
                nums.append(0)
                i+=1
            else:
                break
        return nums
print(Solution().moveZeroes([0,0,0,1,0,3,12,0]))
                