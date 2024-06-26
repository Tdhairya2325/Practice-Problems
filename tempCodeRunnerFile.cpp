// #include<bits/stdc++.h>
// using namespace std;
// #include<iostream>

// int fun(int n)
// {
//         if (n==1 || n==2)
//         return 1;
//         else
//         return fun(n-1)+fun(n-2);
// }

// int main()
// {
//         int x;
//         cin >> x;

//         int a=fun(x);


//         cout <<  a << endl;

//         return 0;   
// }
#include<stdio.h>

void nTriangle(int n) {
	int i,j;
	for(i=0;i<n;i++){
		printf("\n");
          for (j = 0; j <= i; j++) 
            printf("%d ",++i);                    // What is Happening here ???
        }
}
int main()
{
  int n;
  scanf("%d",&n);
  nTriangle(n);
  return 0;
}

