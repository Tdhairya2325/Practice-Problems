#include<stdio.h>

int n;
void main()
{
    printf("Enter a Number:");
    scanf("%d",&n);
    printf("Multiplication Table of 1 to %d\n",n);
for(int i=1;i<=n;i++)
{
    printf("\n");
    for(int j=1;j<=10;j++)
    {
        printf("%d * %d = %d\n",i,j,i*j);
    }
    
}
    
}
