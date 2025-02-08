class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag=list(magazine)
        for letter in ransomNote:
            if letter in mag:
                mag.remove(letter)
            else:
                return False
        return True
print(Solution().canConstruct("aaba","baa"))