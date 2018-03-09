"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
"""

class Solution(object):
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

if __name__ == '__main__':
    a = [4,2,1]
    s = Solution()
    print(s.checkPossibility(a))