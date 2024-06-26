#include <bits/stdc++.h>    
using namespace std;

int main(){
int rev=0,n;
cin >> n;
while(n!=0){
    int digit = n%10;
    rev=rev*10+digit;
     n=n/10;
}
printf("The reverse of the %d is %d",n,rev);
return 0;
}



