def nStarTriangle(n: int) -> None:
      for i in range(n):
         print(' ' * (n - i - 1) + '*' * (2 * i + 1))
      print("\n")
      pass

nStarTriangle(5)

