from typing import List

def printNos(x: int) -> List[int]: 
    if(x>1):
        printNos(x-1)
    print(x,end=" ")
    pass
x=int (input("Enter Num:"))
printNos(x)





# # ______________Reverse Printing_____________

# from typing import List

# def printNos(x: int) -> List[int]:
#     print(x,end=" ")
#     if(x>1):
#         printNos(x-1)
#     return []











# # _____________________Sum of N numbers_____________________

# from typing import List

# def sumFirstN(n: int) :
 
#     if(n==1):
#         return 1
#     else:
#         return n+sumFirstN(n-1)
#     # pass