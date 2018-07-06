# -*- coding: utf-8 -*-
A = [5,1,6,8,2,4,5,10] #原序列

d = [1]*len(A) #用于存放每行的最大长度值
res = 1 #用于记录最终的最大长度
for i in range(len(A)):
    for j in range(i):
#由于一行只记录一个最大值，需要加上判断条件
        if A[i] > A[j] and d[i] < d[j]+1: 
            d[i] = d[j]+1
        if d[i] >  res:
            res = d[i]
print res