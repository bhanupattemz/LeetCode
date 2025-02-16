class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return "" 
        start = 0
        max_length = 1
        for i in range(len(s)):
            odd_length = self.expand_around_center(s, i, i)
            even_length = self.expand_around_center(s, i, i + 1)
            
            length = max(odd_length, even_length)
            
            if length > max_length:
                max_length = length
                start = i - (length - 1) // 2
        
        return s[start:start + max_length]
    
    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1