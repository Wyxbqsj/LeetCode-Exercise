from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def ans(m):
            if m%3==0 and m%5==0:
                return "FizzBuzz"
            else:
                if m%3==0:
                    return "Fizz"
                if m%5==0:
                    return "Buzz"
                else:
                    return str(m)
        res=[]
        for i in range(1,n+1):
            res.append(ans(i))
        return res

x=Solution()
a=x.fizzBuzz(3)
print(a)