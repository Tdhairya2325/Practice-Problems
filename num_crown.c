
//   1             1
//   1 2         2 1
//   1 2 3     3 2 1
//   1 2 3 4 4 3 2 1
#include <stdio.h>
int main()
{
  int n = 5;
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j <= i; j++)
    {
      printf("%d", j + 1);
    }
    for (int k = 0; k < 2*(n-i-1); k++)
    {
      printf(" ");
    } 
    for (int l = i+1; l > 0; l--)
    {
      printf("%d", l);
    }
    printf("\n");
  }
}
