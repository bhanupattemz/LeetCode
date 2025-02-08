class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dups=0
        length=len(nums)
        i=0
        while i<length:
            j=i+1
            if nums[i]!="_":
                while j<length:
                    if nums[i]==nums[j] and nums[j]!="_":
                        nums.remove(nums[j])
                        nums.append("_")
                        dups+=1
                    else:
                        j+=1
            i+=1
        return length-dups
print(Solution().removeDuplicates([1,1,2]))
                        
