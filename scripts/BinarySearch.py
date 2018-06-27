# -*- coding: utf-8 -*-
def BinarySearch_rec(array,item):
    length = len(array)
    if length ==0 : #当长度为0时，即没有找到
        return False
    mid = length / 2
    if array[mid] == item :
        return True
    elif array[mid] > item:
        return BinarySearch_rec(array[:mid],item) #前半数组
    else:
        return BinarySearch_rec(array[mid+1:],item) #后半数组

def BinarySearch(array,item):
    length = len(array)
    start = 0
    end = length-1

    while start <= end :
        mid = (start+end) / 2 #计算每次mid位置
        if array[mid] == item:
            return True
        elif item < array[mid]:
            end = mid - 1 #前半区间S-M
        else:
            start = mid + 1 #后半区间M-E
    return False


if __name__ == '__main__':
    L = [1, 5, 7, 12, 23, 34, 44]
    item = 23
    print "递归实现结果：" , BinarySearch_rec(L,item)

    print "非递归实现结果：" , BinarySearch(L,item)