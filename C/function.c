#include<stdio.h>
int fact(int i)
{
    int f= 1;
    while(i!=0)
    {
        f=f*i;
        i--;
    } return f;
}
int main(){
    int m,n,fm,fn,fmn,c;
    printf("\n enter any value for m & n:");
    scanf("%d%d",&m,&n);
    fm=fact(m);
    fn=fact(n);
    fmn =fact(m-n);
    c=(fm + fn)/ fmn;
    printf("\n c = %d",c);
    return 0;
}