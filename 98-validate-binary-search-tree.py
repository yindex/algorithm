# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.data = []
        self.step(root)
        if len(self.data) == 0:
            return True
        for i in range(0, len(self.data) - 1, 1):
            if self.data[i] >= self.data[i + 1]:
                return False
        return True

    def step(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.data.append(root.val)
            return
        if root.left is not None:
            self.step(root.left)
        self.data.append(root.val)
        if root.right is not None:
            self.step(root.right)


