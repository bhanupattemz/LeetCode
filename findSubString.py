class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        substrings=[]
        result=[]
        for i in range(len(words)):
            item=words[i]
            word=words[0:i]+words[i+1:]
            for j in range(0,len(words)):
                sub=word[0:]
                sub.insert(j,item)
                sub="".join(sub)
                if sub in s:
                    ind=s.index(sub)
                    if ind not in result:
                        result.append(ind)
        return result
        
print(Solution().findSubstring( "barfoofoobarthefoobarman",["bar","foo","the"]))