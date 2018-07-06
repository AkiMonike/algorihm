# -*- coding: utf-8 -*-

def BSearch(array,res,item): #二分查找
    end = res
    start = 0
    while (start <= end):
        mid = start + (end-start)/2
        if array[mid] > item:
            end = mid -1
        elif array[mid] < item:
            start = mid + 1
        else:
            return mid #如果找到元素直接返回
    return start #如果不存在，返回替换元素的位置

def LIS(array):
    res = 1
    d = [0]*len(array)
    d[0] = array[0] #将第一个元素放入临时数组
    for i in array:
        if i > d[res-1]: #如果大于B中最大的，直接插入末尾
            d[res] = i
            res = res + 1
        else:
            pos = BSearch(d,res,i) #如果小于，二分查找位置
            d[pos] = i

    #print d
    return res

if __name__ == '__main__':
    A = [5,1,6,8,2,4,5,10]
    print LIS(A)