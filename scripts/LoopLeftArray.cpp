#include<iostream>  
using namespace std;  
int main()  
{  
    const int n=7,k=3;  
    char a[n]={'a','b','c','d','e','f','g'};  
    char b[k];  
    int i;  
    for(i=0;i<k;i++)b[i]=a[i];          //将前k个放到新的数组里
    for(;i<n;i++)a[i-k]=a[i];           //将后边的元素前移
    for(i=0;i<k;i++)a[n-k+i]=b[i];      //将前k个元素放到末尾
    for(i=0;i<n;i++)cout<<a[i]<<" ";  
    cout<<endl;  
}   
