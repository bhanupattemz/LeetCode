class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
            n1=i%3==0
            n2=i%5==0
            result.append("FizzBuzz" if n1 and n2 else "Fizz" if n1 else "Buzz" if n2 else f"{i}")
        return result
        