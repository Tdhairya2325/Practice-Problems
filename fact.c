// "Factorial of N"

#include<stdio.h>

int a;
int fact(int n)
{
    if(n==1)
    {
        return 1; 
    }
    else
    {
        a=n*fact(n-1);
        return a;
    }
}

void main()
{
    int x;
    printf("Enter no to find Factorial:");
    scanf("%d",&x);
    fact(x);
    printf("\nThe factorial of %d is %d",x,a);
}



