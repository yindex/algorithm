# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        l = 0
        while p is not None:
            p = p.next
            l += 1
        k %= l

        if head is None:
            return None

        k += 1
        self.head = head
        self.tail = head
        current = head

        while current.next is not None:
            if k == 1:
                self.tail = current
            if k == 0:
                self.head = current
            current = current.next
            k -= 1
        current.next = head
        self.tail.next = None
        return self.head

if __name__ == '__main__':
    data = [2,3,4,5]
    head = ListNode(1)
    f = head
    for i in data:
        head.next = ListNode(i)
        head = head.next

    f = Solution().rotateRight(f, 2)

    while f is not None:
        print(f.val)
        f = f.next