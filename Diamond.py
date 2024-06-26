def nStarDiamond(n: int) -> None:
    for i in range(n):
        print(' ' * (n-i-1) + '*' * (2*i+1))
    for i in range(n,0,-1):
        print(' ' * (n-i) + '*' * (2*i-1))   
    print("\n")
    pass


nStarDiamond(5)