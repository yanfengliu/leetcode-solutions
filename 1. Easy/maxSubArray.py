# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# https://leetcode.com/problems/maximum-subarray/description/

# ============================================================================================
# Main idea: 
# This problem can be solved with dynamic programming technique. We make the observation that at every 
# position in the array, the maximum subarray either includes it or doesn't. We take the bigger of the 
# two and achieves global optimum. In practice this is equivalent to filling out a n by 2 table, where 
# n = len(nums). The left column has the max subarray so far that includes the i th number, and the 
# right column has the max subarray so far that exclude it. 

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
            # create a n by 2 table. The meaning of this is explained in the "mean idea" section. 
            a = [[], []] * len(nums)
            a[0] = nums[n-1]
            a[1] = -float('inf')
            for i in range(1, len(nums)):
                # if the previous max subarray including the i-1 th number sums up to be greater 
                # than or equal to 0
                if a[2*(i-1)] >= 0:
                    # then the current best max subarray including the i th number should be the 
                    # current number appended to the previous one
                    a[2*i] = nums[n-1-i] + a[2*(i-1)]
                else:
                    # otherwise, the current best max subarray is just the current number itself,
                    # since adding it to the previous max subarray, which is negative, will be 
                    # not optimal
                    a[2*i] = nums[n-1-i]
                # the max subarray excluding the current number is simply the larger of the two
                # numbers from the previous iteration
                a[2*i+1] = max([a[2*(i-1)], a[2*(i-1)+1]])
            # in the end, return the larger of the two max subarrays (including or excluding the
            # last number), and obtain the true max subarray
            return max([a[2*(n-1)], a[2*(n-1)+1]])
        
