n= int(input())
def reverse(n):
    sign = 1 if n >= 0 else -1
    x=n
    n=abs(n)
    rev=0
    while n>0:
        digit = n % 10
        rev = rev*10 + digit
        n//=10
    if rev > 2**31-1 or rev < -2**31: 
        return 0
    # print(rev)
    y=rev*sign
    # print(x,y)
    if(y==x): print("true")
    else: print ("false")
reverse(n)


# class Solution:
#     x=int(input())
#     def isPalindrome(self, x: int) -> bool:
#         sign = 1 if x >= 0 else -1
#         n=x
#         x=abs(x)
#         rev=0
#         while x>0:
#             digit = x % 10
#             rev = rev*10 + digit
#             x//=10
#         if rev > 2**31-1 or rev < -2**31: 
#             return 0
#     # print(rev)
#         y=rev*sign
#     # print(x,y)
#         if(y==n): print("true")
#         else: print ("false")
#     isPalindrome(self,x)