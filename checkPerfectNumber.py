class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum=1
        for i in range(2,num//2+1):
            if(num%i==0):
                sum+=i
        return num==sum
                
print(Solution().checkPerfectNumber(28))