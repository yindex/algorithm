# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        current = head
        while l1 and l2:
            val = l1.val + l2.val + carry
            current.next = ListNode(val % 10)
            carry = val / 10
            current = current.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry
            current.next = ListNode(val % 10)
            carry = val / 10
            current = current.next
            l1 = l1.next
        while l2:
            val = l2.val + carry
            current.next = ListNode(val % 10)
            carry = val / 10
            current = current.next
            l2 = l2.next
        if carry != 0:
            current.next = ListNode(carry)
        return head.next

