# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/add-two-numbers/description/

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0);
        if (l1 == None) and (l2 != None):
            l3 = l2
        elif (l1 != None) and (l2 == None):
            l3 = l1
        elif (l1 == None) and (l2 == None):
            l3 = None
        else:
            sum_val = l1.val + l2.val
            if (sum_val >= 10):
                l3.val = sum_val - 10
                l1.next = self.addTwoNumbers(l1.next, ListNode(1))
                l3.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                l3.val = sum_val
                l3.next = self.addTwoNumbers(l1.next, l2.next)
        return l3
        
