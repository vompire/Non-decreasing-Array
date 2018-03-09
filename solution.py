# -*- coding: utf-8 -*-
"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
"""

class Solution1(object):
    """这种方法有误，利用list求和无法判断是否存在元素相减小于0的情况"""
    def checkPossibility(self, nums):
        flag = False
        for i in range(len(nums)-1):
            item = nums[i]
            if flag is False:
                if sum(list(map(lambda x:x[0]-x[1], zip(nums[i+1:],[item]*(len(nums)-1-i))))) != len(nums[i+1:]):
                    flag = True
            else:
                if sum(list(map(lambda x:x[0]-x[1], zip(nums[i+1:],[item]*(len(nums)-1-i))))) != len(nums[i + 1:]):
                    return False
        return True

class Solution2(object):
    """首先比较相邻两个位置元素的大小，如果不存在前项大于后项，返回true,如果存在两个前项大于后项，
    返回false，如果存在一个前项大于后项，做讨论：出现A[i] > A[i+1]这种情况只会有两个问题1.A[i]异常2.A[i+1]异常，
    return分别用来测试这种异常是否是可容忍的范围之内 """
    """算法思想的核心是一旦确立了两个异常点，这两个点以外的序列的顺序是正常的，按照从小到大"""
    def checkPossibility(self, A):
        p = None
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])

if __name__ == '__main__':
    a = [4,2,1]
    s = Solution2()
    print(s.checkPossibility(a))