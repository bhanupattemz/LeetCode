class Solution:
    def countSegments(self, s: str) -> int:
        s=s.strip()
        result=0
        for w in s.split(" "):
            if w!=" " and w!="":
                result +=1
        return result
        