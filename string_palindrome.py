class Solution:

    def isPalindrome(s: str) -> bool:
        no_punct = "".join(char for char in s if char.isalnum())
        no_punct=no_punct.lower()
        print(no_punct)
        x=""
        for i in no_punct:
            x=i+x
        if (no_punct==x):
            print("true")
        else:
            print("false")

    s="Madam I'm Adam"
    # s=" "
    isPalindrome(s)
        




# def isPalindrome(s):
#     left = 0
#     right = len(s)-1
#     while left < right:
#         if not s[left].isalnum():
#             left += 1
#         elif not s[right].isalnum():
#             right -= 1
#         elif s[left].lower() != s[right].lower():
#             return False
#         else:
#             left += 1
#             right -= 1
#     return True
        