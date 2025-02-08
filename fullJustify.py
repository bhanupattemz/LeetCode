class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        finList=[]
        line=[]
        length=0
        for item in words:
            length+=len(item)+1
            if length>maxWidth:
                finList.append(" ".join(line))
                line=[item]
                length=len(item)+1
            else:
                line.append(item)
        finList.append(" ".join(line))
        for i in range(len(finList)):
            
            j=0
                
            while len(finList[i])<maxWidth:
                if i==len(finList)-1:
                    finList[i]+=" "
                else:
                    add=" "
                    sub=""
                    line=finList[i]
                    for j in range(len(finList[i])):
                        sub+=line[j]
                        if line[j]==add and len(sub+line[j+1:])<maxWidth:
                            sub+=add
                    add+=" "
                    finList[i]=sub
        return finList
print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))