# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].

# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_val = 0
        max_idx = 0
        for i in range(len(nums)):
            current_val = nums[i]
            if (current_val >= max_val):
                max_val = current_val
                max_idx = i
        node = TreeNode(max_val)
        left = nums[:max_idx]
        right = nums[max_idx+1:]
        if left:
            node.left = self.constructMaximumBinaryTree(left)
        if right:
            node.right = self.constructMaximumBinaryTree(right)
        return node