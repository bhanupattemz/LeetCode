import math
class Solution:
    def reverse(self, x: int) -> int:
        if(x<-math.pow(2,31) or x>math.pow(2,31)-1):
            return 0
        result=str(abs(x))
        result=int(result[::-1])
        if(x<0):
            result=-1*result
        if(result<-math.pow(2,31) or result>math.pow(2,31)-1):
            return 0
        return result

            
        