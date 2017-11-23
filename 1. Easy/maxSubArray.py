# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import numpy as np
        
        if len(nums) == 1:
            return(nums[0])
        else:
            n = len(nums)
            a = [[], []] * len(nums)
            a[0] = nums[n-1]
            a[1] = -float('inf')
            for i in range(1, len(nums)):
                if a[2*(i-1)] >= 0:
                    a[2*i] = nums[n-1-i] + a[2*(i-1)]
                else:
                    a[2*i] = nums[n-1-i]
                a[2*i+1] = max([a[2*(i-1)], a[2*(i-1)+1]])
            return max([a[2*(n-1)], a[2*(n-1)+1]])
        
