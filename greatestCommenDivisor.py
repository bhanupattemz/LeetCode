class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Helper function to compute GCD of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # If concatenating the strings in different orders gives different results,
        # there's no common divisor string
        if str1 + str2 != str2 + str1:
            return ""
        
        # The GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # The GCD string would be the prefix of str1 (or str2) with the length of gcd_length
        return str1[:gcd_length]

            
print(f'answer:{Solution().gcdOfStrings("ABABCCABAB","ABAB")}')
                