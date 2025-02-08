class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        deletes=0
        prev=''
        count=0
        i=0
        l=len(nums)
        while i<l:
            if nums[i]=="_":
                break
            if nums[i]==prev:
                count+=1
                if count>1:
                    del nums[i]
                    nums.append("_")
                    i-=1
                    deletes+=1
            else:
                prev=nums[i]
                count=0
            i+=1
        return l-deletes
print(Solution().removeDuplicates([0,0,0,0,0]))