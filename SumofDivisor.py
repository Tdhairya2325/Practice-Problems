# def sumOfAllDivisors(n: int) -> int:
#     a=0
#     for i in range(n,0,-1):
#         for j in range(n):
#             if (n % (j+1) == 0):
#                 a=a+(j+1)
#         n-=1
#         print(n)
#         # print(j)
#         # print(i)       
#         print("Sum:",a)
# n= int(input("Enter Number:"))            
# sumOfAllDivisors(n)






# optimized
def sumOfAllDivisors(n: int) -> int:

  if n <= 1:
    return n

  sum_of_divisors = 1 + n
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      # Add both the divisor and its corresponding pair (n / divisor)
      # if they are different (e.g., for n = 12, add 3 and 4).
      sum_of_divisors += i + (n // i if n // i != i else 0)
  print(sum_of_divisors)
  return sum_of_divisors

sumOfAllDivisors(64)
