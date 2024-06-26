class Solution:
    def reverse(x):
        rev=0
        while x>0:
            digit = x % 10
            rev = rev*10 + digit
            x//=10
        print(rev) 
    reverse(64866)