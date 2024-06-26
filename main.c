#include <stdio.h>


char str1[],str2[],str3[];
char len1[],len2[],len3[];
int i,j;
void main(int argc, char const *argv[])
{
    len1[]=strlen(str1);
    len2[]=strlen(str2);
    while(i<len1-1)
    {
        str3[i]=str1[i];
        i++;
    }
j=0;
while(i<len1+len2-2)
{
    str3[i]=str2[j];
    j++;
    i++;
}

}
