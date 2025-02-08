class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l1=len(flowerbed)
        i=0
        if flowerbed[0]==0 :
            if(l1==1):
                flowerbed[0]=1
                n-=1
            elif flowerbed[1]==0:
                flowerbed[0]=1
                n-=1
        if flowerbed[l1-1]==0 and flowerbed[l1-2]==0:
            flowerbed[l1-1]=1
            n-=1
        while i<=l1-2:
            if flowerbed[i-1:i+2]==[0,0,0]:
                flowerbed[i]=1
                n-=1
                i+=1
            i+=1
            
        return True if n<=0 else False
print(Solution().canPlaceFlowers([0,0,1,0,0],1))
            