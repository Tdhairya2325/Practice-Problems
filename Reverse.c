
#include<stdio.h>

    // int main()
    // {
    //     int arr[6]={1,2,3,4,5,6},n,a;
        
    //     n=sizeof(arr)/sizeof(arr[0]);

    //     for(int i=arr[n-1];i>0;i--)
    //     {
    //         // scanf("%d",&arr);
    //         printf("%d\n",arr[i]);
    //     }
    //     return 0;
    // }

int main() {
int arr[10] = {1, 2, 3, 4, 5,6,7,8,9,100},i;
int n = sizeof(arr) / sizeof(arr[0]);
  for (i=arr[n-1]; i >=0; i--) {
    printf("___%d___\n", arr[i]);
  }

  return 0;
}