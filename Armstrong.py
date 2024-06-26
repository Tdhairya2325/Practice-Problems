

def checkArmstrong(n):
  original_n=n
  a=0
  l=len(str(n))
  while n >0:
    digit=n%10
    a+=(digit**l)
    # print("Sum:",a)
    n=n//10
    # print("n:",n)
  if(a!=original_n):
    return False 
  return True 
n= int (input("Entar Number:"))
checkArmstrong(n)










# def checkArmstrong(n):
#   """Checks if a number is an Armstrong number.

#   Args:
#       n: The integer to check.

#   Returns:
#       True if n is an Armstrong number, False otherwise.
#   """
#   original_n = n
#   a = 0
#   l = len(str(n))
#   while n > 0:
#     digit = n % 10
#     a += digit**l
#     n //= 10
#     # Early return optimization (optional)
#     if a > original_n:
#       return False

#   return a == original_n

# # Example usage
# number = int (input())
# result = checkArmstrong(number)
# print(f"{number} is an Armstrong number: {result}")
