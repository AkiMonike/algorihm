#!/usr/bin/python 

len = 5
a = [3,4,5,2,1]

for i in range(len-1):
  	for j in range(len-1-i):
		if a[len-1-j] < a[len-1-j-1]: 
			a[len-1-j], a[len-1-j-1] = a[len-1-j-1], a[len-1-j]
print a