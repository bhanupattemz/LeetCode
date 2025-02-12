class Solution:
    def maxDifference(self, s: str) -> int:
        dis = {}
        for l in s:
            if l in dis:
                dis[l] += 1
            else:
                dis[l] = 1
        min_even,max_even = 100,0
        min_odd,max_odd = 100,0
        for key,item in dis.items():
            if(item%2==0):
                if(item<min_even):
                    min_even=item
                if item>max_even:
                    max_even=item
            else:
                if(item<min_odd):
                    min_odd=item
                if item>max_odd:
                    max_odd=item
        return max(max_even-min_odd,max_odd-min_even)
print(Solution().maxDifference("aaaaabbc"))