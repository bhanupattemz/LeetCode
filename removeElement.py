class Solution(object):
    def removeElement(self, nums, val):
        times,i=0,0
        while True:
            
            if nums[i]=="_" or i>=len(nums):
                print(nums)
                return len(nums)-times
            elif(nums[i]==val):
                times+=1
                nums.remove(nums[i])
                nums.append("_")
            else:
                i+=1
           

        
print(Solution().removeElement([0,1,2,2,3,0,4,2],2))