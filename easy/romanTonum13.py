class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        s=s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
        while i<len(s):
                result+=roman[s[i]]
                i+=1
        return result

            
print(Solution().romanToInt("MCMXCIV"))
