class Solution:
    def reverseVowels(self, s: str) -> str:
        l=len(s)
        s=list(s)
        i,j=0,l-1
        vowels=['a', 'e', 'i', 'o','u']
        while i<l and j>=0 and i<=j:
            if not (s[i].lower() in  vowels):
                i+=1
            if not (s[j].lower() in vowels):
                j-=1
            if(s[j].lower() in vowels and s[i].lower() in vowels and i<=j):
                s[j],s[i]=s[i],s[j]
                i+=1
                j-=1
        return "".join(s)

print(Solution().reverseVowels("race a car"))