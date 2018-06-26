#include<iostream>  
using namespace std;  
void Reverse(char *a,int left,int right)  
{  
    int mid = (left+right)/2;  
    char temp;  
    for(int i=0;i<=(mid-left);i++)  
    {  
        temp = a[left+i];  
        a[left+i] = a[right-i];  
        a[right-i]= temp;     
    }  
} 

int main()  
{  
    const int n=7,k=3;  
    char a[n]={'a','b','c','d','e','f','g'};   
    Reverse(a,0,n-1-k); //对A进行逆置  
    Reverse(a,n-k,n-1); //对B进行逆置  
    Reverse(a,0,n-1);   //对A^-1 B^-1进行逆置
    for(int i=0;i<n;i++)cout<<a[i]<<" ";  
    cout<<endl;   
}   