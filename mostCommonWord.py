class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        temp=paragraph.split(" ")
        result={}
        max=0
        word=None
        for w in temp:
            if(w=="" or w==" "):
                continue
            if(',' in w):
                w=w.removesuffix(',')
            if "." in w :
                w=w.removesuffix(".")
            w=w.lower()
            if w in banned:
                continue
            if(w in result):
                result[w]+=1
            else:
                result[w]=1
            if result[w]>max:
                    max=result[w]
                    word=w
                
        return word
print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))