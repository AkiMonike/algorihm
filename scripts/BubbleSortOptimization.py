#!/usr/bin/python 
len = 5
a = [3,4,5,2,1]
flag = 1 #默认为有序
for i in range(len-1):
	flag = 1
  	for j in range(len-1-i):
		if a[len-1-j] < a[len-1-j-1]: 
			a[len-1-j], a[len-1-j-1] = a[len-1-j-1], a[len-1-j]
			flag =0 #如果发生交换设置为无序
	if flag == 1 :
		break;
print a