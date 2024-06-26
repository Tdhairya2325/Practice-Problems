#include <stdio.h>
#include<string.h>



char str1[]="Dhairya",str2[]="Trivedi",str3[]="";
int  len1,len2,len3;
int i,j;
void main()
{
    len1=strlen(str1);
    len2=strlen(str2);
    while(i<=len1-1)
    {
        str3[i]=str1[i];
        i++;
    }
    j=0;
    while(i<=len1+ len2-1)
    {
    str3[i]=str2[j];
        j++;
        i++;
    }
   
printf("%s\n",str3);
}
