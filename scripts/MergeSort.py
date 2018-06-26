# -*- coding: utf-8 -*-
def merge(left, right):
    llen = len(left)
    lcur = 0
    rlen = len(right)
    rcur = 0
    result = []
    while lcur < llen and rcur < rlen:
        lone = left[lcur]
        rone = right[rcur]
        result.append(min(lone, rone))
        if lone < rone:
            lcur += 1
        else:
            rcur += 1
    result += left[lcur:]
    result += right[rcur:]
    return result

def msort_rec(array):
    length = len(array)
    if length == 1:
        return array
    else:
        mid = length / 2
        left = msort_rec(array[0: mid])
        right = msort_rec(array[mid: length])
        return merge(left, right)

def msort_iter(array):
    length = len(array)
    step = 1
    while step < length:
        for left in range(0, length - step, 2 * step):
            result = merge(array[left:left + step],
                           array[left + step: min(left + 2 * step,
                                                  length)])
            array = array[0:left] + result + array[min(left + 2 *
                                                       step, length):]
        step = step * 2
    return array

if __name__ == '__main__':
    L = [1, 4, 2, 6, 3, 5, 8, 7]
    print "排序前: %r" %(L)
    R = msort_rec(L)
    print "排序后(递归): %r" %(R)
    I = msort_iter(L)
    print "排序后(非递归): %r" %(I)