# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        