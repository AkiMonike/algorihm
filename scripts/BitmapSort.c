#include <stdio.h>
#define MAX 10000000
#define MASK 0x1F //32的二进制表示
#define DIGITS 32 //设置为32位
#define SHIFT 5    //由于32=2^5

int bitmap[1+MAX/DIGITS];

void setbit(int n)     //将逻辑位置为n的二进制位置为1
{
    bitmap[n>>SHIFT] |= (1<<(n&MASK)); //n>>SHIFT右移5位相当于除以32求算字节位置，n&MASK相当于对32取余即求位位置，
}         //然后将1左移的结果与当前数组元素进行或操作，相当于将逻辑位置为n的二进制位置1.

void initbit(int n)
{
    bitmap[n>>SHIFT] &= ~(1<<(n&MASK)); //将逻辑位置为n的二进制位置0，原理同set操作
}

int test(int n)
{
    return bitmap[n>>SHIFT] & (1<<(n&MASK));  //测试逻辑位置为n的二进制位是否为1
}

int main(int argc, char *argv[])
{
    int i,n;
    for(i=0;i<MAX;i++)
    {
        initbit(i);
    }
    while(scanf("%d",&n)!=EOF)
    {
        setbit(n);
    }
    for(i=0;i<MAX;i++)
    {
        if(test(i))
            printf("%d ",i);
    }
    return 0;
}
