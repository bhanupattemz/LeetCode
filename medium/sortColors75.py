class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # # l=len(nums)
        # # for i in range(l):
        # #     for j in range(i+1,l):
        # #         if nums[i]>nums[j]:
        # #             nums[i],nums[j]=nums[j],nums[i]
        # # return nums
        # def merge(nums,start, mid,end):
        #     l1=mid-start+1
        #     l2=end-mid
        #     # list1,list2=[],[]
        #     # [list1.append(nums[start+k]) for k in range(0,l1) ]
        #     # [list2.append(nums[mid+1+k]) for k in range(0,l2)]
        #     i,j=0,0
        #     list1=nums[start:mid+1]
        #     list2=nums[mid+1:end+1]
        #     k=start
        #     while i<l1 and j <l2:
        #         if list1[i]>list2[j]:
        #             nums[k]=list2[j]
        #             j+=1
        #         else:
        #             nums[k]=list1[i]
        #             i+=1
        #         k+=1
        #     while i<l1:
        #         nums[k]=list1[i]
        #         k+=1
        #         i+=1
        #     while j<l2:
        #         nums[k]=list2[j]
        #         k+=1
        #         j+=1
        
        # def mergesort(nums,start,end):
        #     if start<end:
        #         mid=start+(end-start)//2
        #         mergesort(nums,start,mid)
        #         mergesort(nums,mid+1,end)
        #         merge(nums,start,mid,end)
        # mergesort(nums,0,len(nums)-1)
        # return nums
        zero=0
        one=0
        two=0
        for num in nums:
            if num==0:
                zero+=1
            elif num==1:
                one+=1
            else:
                two+=1
        # list=[0]*zero+[1]*one+[2]*two
        # for i in range(len(nums)):
        #     nums[i]=list[i]
        k=0
        while k<zero:
            nums[k]=0
            k+=1
        while k<one+zero:
            nums[k]=1
            k+=1
        while k<two+one+zero:
            nums[k]=2
            k+=1
        return nums
print(Solution().sortColors([2,0,2,1,1,0]))