
// "GCD of N"
#include<stdio.h>
int m;
int gcd(int m,int n)
{
    while(n!=0)
    {
        int r= m % n;
        m=n;
        n=r;
    }
    return m;
}

int main()
{
    int x,y;
    printf("Enter numbers to find GCD:");
    scanf("%d,%d",&x,&y);
    m=gcd(x,y);
    printf("GCD of %d and %d is %d",x,y,m);
    return 0;
}
