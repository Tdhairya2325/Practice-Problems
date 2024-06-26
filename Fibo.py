class Solution:
    def fibo(self,n: int) -> int:
        if (n==1):
            return 1
        if (n==0):
            return 0
        x = self.fibo(n-1) + self.fibo(n-2)
        return x    