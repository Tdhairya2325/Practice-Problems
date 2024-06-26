def nStarTriangle(n: int) -> None:
    for i in range(n):
        print( '*' * (i))
    for i in range(n,0,-1):
        print( '*' * (i))   
    print("\n")
    pass

nStarTriangle(4)